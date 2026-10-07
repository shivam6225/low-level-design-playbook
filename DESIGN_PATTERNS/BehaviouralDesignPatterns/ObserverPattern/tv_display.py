from DESIGN_PATTERNS.BehaviouralDesignPatterns.ObserverPattern.observer import Observer


class TVDisplay(Observer):
    def update(self,new_temp):
        print("TV temperature updated to {}".format(new_temp))