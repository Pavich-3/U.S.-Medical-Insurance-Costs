import csv

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

def load_data(lst, file, column):
    with open(file) as project_file:
        my_data = csv.DictReader(project_file)
        for row in my_data:
            lst.append(row[column])


load_data(age, "insurance_project.csv", "age")
load_data(sex, "insurance_project.csv", "sex")
load_data(bmi, "insurance_project.csv", "bmi")
load_data(children, "insurance_project.csv", "children")
load_data(smoker, "insurance_project.csv", "smoker")
load_data(region, "insurance_project.csv", "region")
load_data(charges, "insurance_project.csv", "charges")

class PatiensInfo:
    def __init__(self, list_ages, list_sex, list_bmi, list_children, list_smoker, list_region, list_charges):
        self.list_ages = list_ages
        self.list_sex = list_sex
        self.list_bmi = list_bmi
        self.list_children = list_children
        self.list_smoker = list_smoker
        self.list_region = list_region
        self.list_charges = list_charges


# average age of the patients
    def avg_age(self):
        total_age = 0
        for age in self.list_ages:
            total_age += int(age)
        average = total_age / len(self.list_ages)
        return "The average age is " + str(round(average, 1)) + " years old."


# how many smokers and non-smokers
    def coun_smoker(self):
        people_smok = self.list_smoker.count('yes')
        people_non_smok = self.list_smoker.count('no')
        return "People who smoker are: " + str(people_smok), "People who non-smoker are: " + str(people_non_smok)


# where a majority of the individuals are from
    def maj_region(self):
        our_region = []
        for region in self.list_region:
            if not region in our_region:
                our_region.append(region)

        total_region = 0
        name_region = ""
        for i in range(0, len(our_region)):
            count_total = self.list_region.count(our_region[i])
            if count_total > total_region:
                total_region = count_total
                name_region = our_region[i]

        return "A majority of the individuals are from " + name_region + " and there are: " + str(total_region)


    # who more, male or female from patiens
    def count_sex(self):
        counter_male = 0
        counter_female = 0
        for sex in self.list_sex:
            if sex == "male":
                counter_male += 1
            else:
                counter_female += 1

        return "The female are: " + str(counter_female), "The male are: " + str(counter_male)


    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.list_ages]
        self.patients_dictionary["sex"] = self.list_sex
        self.patients_dictionary["bmi"] = self.list_bmi
        self.patients_dictionary["children"] = self.list_children
        self.patients_dictionary["smoker"] = self.list_smoker
        self.patients_dictionary["regions"] = self.list_region
        self.patients_dictionary["charges"] = self.list_charges
        return self.patients_dictionary


    # how does the number of children affect the cost
    def infl_child(self):
        how_child = {child: charge for child, charge in zip(self.list_children, self.list_charges)}
        child_dict = {charg: child for charg, child in zip(self.list_charges, self.list_children)}
        smoker_dict = {charg: smoker for charg, smoker in zip(self.list_charges, self.list_smoker)}
        total_cost_1 = 0
        total_cost_5 = 0
        list_len_1 = []
        list_len_5 = []
        for value in smoker_dict.values():
            if value == "no": #without smokers
                for key, val in child_dict.items():
                    if val == "1":
                        total_cost_1 += float(key)
                        list_len_1.append(key)
                    elif val == "5":
                        total_cost_5 += float(key)
                        list_len_5.append(key)

        differences = round(total_cost_5 / len(list_len_5) - total_cost_1 / len(list_len_1), 2)
        total_cost_1_round = round(total_cost_1, 2)
        total_cost_5_round = round(total_cost_5, 2)
        print(sorted(how_child.keys()))
        print(f"If we have 1 children, our total cost: {total_cost_1_round}. If we have 5 children, out total cost: {total_cost_5_round}. Our differences: {differences} between 5 to 1 children.")


a = PatiensInfo(age, sex, bmi, children, smoker, region, charges)
a.infl_child()

# different costs between smokers vs. non-smokers.
def calcul_costs(file):
    list_smoker_costs = []
    list_non_smoker_costs = []
    with open(file) as project_file:
        my_data = csv.DictReader(project_file)
        for row in my_data:
            if row["smoker"] == "yes":
                list_smoker_costs.append(row["charges"])
            elif row["smoker"] == "no":
                list_non_smoker_costs.append(row["charges"])

    total_cost_smoker = 0
    for cost in list_smoker_costs:
        total_cost_smoker += float(cost)

    total_cost_non_smoker = 0
    for cost in list_non_smoker_costs:
        total_cost_non_smoker += float(cost)

    avg_smoker = total_cost_smoker / len(list_smoker_costs)
    avg_non_smoker = total_cost_non_smoker / len(list_non_smoker_costs)

    difference = avg_smoker - avg_non_smoker
    return "Costs between smokers vs non-smokers: " + str(round(difference, 2))  # we calculated the difference between the mean


# what the average age is for someone who has at least one child in this dataset
def avg_age_par(file):
    parent_age = []
    with open(file) as project_file:
        my_data = csv.DictReader(project_file)
        for row in my_data:
            if int(row["children"]) >= 1:
                parent_age.append(row["age"])

    total_age = 0
    for age in parent_age:
        total_age += int(age)

    avg_par = total_age / len(parent_age)
    return "The average age is for someone who has at least one child: " + str(round(avg_par, 1))
