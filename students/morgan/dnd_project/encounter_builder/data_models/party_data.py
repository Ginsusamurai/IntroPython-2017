class Party:
    def __init__(self, members):

        #members is a list of levels, no class info ie [3,3,3,5,5]
        self.members = members
        self.min = min(members)
        self.crowd = len(members)
        self.easy = 0
        self.medium = 0
        self.hard = 0
        self.deadly = 0
        self.easy_cr = []
        self.medium_cr = []
        self.hard_cr = []
        self.deadly_cr = {}
        self.monster_variety = 1

    def set_budgets(self, easy, medium, hard, deadly):
        self.easy = easy
        self.medium = medium
        self.hard = hard
        self.deadly = deadly

    def set_cr_ranges(self, easy_cr, medium_cr, hard_cr, deadly_cr):
        self.easy_cr = easy_cr
        self.medium_cr = medium_cr
        self.hard_cr = hard_cr
        self.deadly_cr = deadly_cr

    def monster_types(self, group_size):
        split = 0
        if group_size > 1:
            while True:
                split = input("How many types of monsters do you want? (Must be less or equal to {}\n>".format(group_size))
                try:
                    split = int(split)
                    if split > group_size:
                        print("Please enter a value less than {}".format(group_size))
                    else:
                        self.monster_variety = split
                        break
                except ValueError:
                    print("Please enter an integer")
                    pass
                except TypeError:
                    print("Please enter an integer")
                    pass
        # print(self.monster_variety)