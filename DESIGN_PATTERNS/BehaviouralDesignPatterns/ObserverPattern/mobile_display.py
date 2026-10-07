from DESIGN_PATTERNS.BehaviouralDesignPatterns.ObserverPattern.observer import Observer


class MobileDisplay(Observer):
    def update(self,new_temp):
        print("Mobile temperature updated to {}".format(new_temp))