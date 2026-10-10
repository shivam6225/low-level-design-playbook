from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from Food import *

if TYPE_CHECKING:
    from DESIGN_PATTERNS.CreationalDesignPatterns.AbstractFactoryPattern.GoodExample.Dessert import Dessert
    from DESIGN_PATTERNS.CreationalDesignPatterns.AbstractFactoryPattern.GoodExample.MainCourse import MainCourse
    from DESIGN_PATTERNS.CreationalDesignPatterns.AbstractFactoryPattern.GoodExample.Starter import Starter


class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self) -> "Starter":
        pass

    @abstractmethod
    def create_main_course(self) -> "MainCourse":
        pass

    @abstractmethod
    def create_dessert(self) -> "Dessert":
        pass


class NorthIndianCuisineFactory(CuisineFactory):
    def create_starter(self) -> "Starter":
        return PaneerTikka()
    def create_main_course(self) -> "MainCourse":
        return ButterChicken()
    def create_dessert(self) -> "Dessert":
        return GulabJamun()

class SouthIndianCuisineFactory(CuisineFactory):
    def create_starter(self) -> "Starter":
        return MeduVada()
    def create_main_course(self) -> "MainCourse":
        return Dosa()
    def create_dessert(self) -> "Dessert":
        return Payasam()