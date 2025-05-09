from enum import Enum
from typing import Any, List, Optional, Sequence, Union

from flet.core.adaptive_control import AdaptiveControl
from flet.core.alignment import Alignment
from flet.core.animation import AnimationValue
from flet.core.constrained_control import ConstrainedControl
from flet.core.control import Control, OptionalNumber
from flet.core.ref import Ref
from flet.core.types import (
    ClipBehavior,
    OffsetValue,
    OptionalControlEventCallable,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)


class StackFit(Enum):
    LOOSE = "loose"
    EXPAND = "expand"
    PASS_THROUGH = "passThrough"


class Stack(ConstrainedControl, AdaptiveControl):
    """
    A control that positions its children on top of each other.

    This control is useful if you want to overlap several children in a simple way, for example having some text and an image, overlaid with a gradient and a button attached to the bottom.

    Stack is also useful if you want to implement implicit animations (https://flet.dev/docs/guides/python/animations/) that require knowing absolute position of a target value.

    Example:

    ```
    import flet as ft

    def main(page: ft.Page):
        st = ft.Stack(
            controls=[
                ft.Image(
                    src=f"https://picsum.photos/300/300",
                    width=300,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            "Image title",
                            color="white",
                            size=40,
                            weight="bold",
                            opacity=0.5,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            width=300,
            height=300,
        )

        page.add(st)

    ft.app(target=main)
    ```

    -----

    Online docs: https://flet.dev/docs/controls/stack
    """

    def __init__(
        self,
        controls: Optional[Sequence[Control]] = None,
        clip_behavior: Optional[ClipBehavior] = None,
        alignment: Optional[Alignment] = None,
        fit: Optional[StackFit] = None,
        #
        # ConstrainedControl and AdaptiveControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: Optional[RotateValue] = None,
        scale: Optional[ScaleValue] = None,
        offset: Optional[OffsetValue] = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: Optional[AnimationValue] = None,
        animate_size: Optional[AnimationValue] = None,
        animate_position: Optional[AnimationValue] = None,
        animate_rotation: Optional[AnimationValue] = None,
        animate_scale: Optional[AnimationValue] = None,
        animate_offset: Optional[AnimationValue] = None,
        on_animation_end: OptionalControlEventCallable = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        adaptive: Optional[bool] = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        AdaptiveControl.__init__(self, adaptive=adaptive)

        self.__controls: List[Control] = []
        self.controls = controls
        self.clip_behavior = clip_behavior
        self.alignment = alignment
        self.fit = fit

    def _get_control_name(self):
        return "stack"

    def _get_children(self):
        return self.__controls

    def before_update(self):
        super().before_update()
        self._set_attr_json("alignment", self.__alignment)

    def __contains__(self, item):
        return item in self.__controls

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value: Optional[Sequence[Control]]):
        self.__controls = list(value) if value is not None else []

    # clip_behavior
    @property
    def clip_behavior(self) -> Optional[ClipBehavior]:
        return self.__clip_behavior

    @clip_behavior.setter
    def clip_behavior(self, value: Optional[ClipBehavior]):
        self.__clip_behavior = value
        self._set_enum_attr("clipBehavior", value, ClipBehavior)

    # alignment
    @property
    def alignment(self) -> Optional[Alignment]:
        return self.__alignment

    @alignment.setter
    def alignment(self, value: Optional[Alignment]):
        self.__alignment = value

    # fit
    @property
    def fit(self) -> Optional[StackFit]:
        return self.__fit

    @fit.setter
    def fit(self, value: Optional[StackFit]):
        self.__fit = value
        self._set_enum_attr("fit", value, StackFit)
