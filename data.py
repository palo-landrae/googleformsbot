import random as rd


class Data:
    def __init__(self, n):
        self.age_range = [0, 1, 2, 3, 4, 5]
        self.gender = [2, 1, 0]
        self.places = ["Agoncillo", "Alitagtag", "Balayan", "Balete", "Batangas City", "Bauan", "Calaca", "Calatagan", "Cuenca", "Ibaan", "Laurel", "Lemery", "Lian", "Lipa CIty", "Lobo", "Mabini", "Malvar", "Mataasnakahoy",
                       "Nasugbu", "Padre Garcia", "Rosario", "San Jose", "San Juan", "San Luis", "San Nicolas", "San Pascual", "Santa Teresita", "Santo tomas City", "Taal", "Talisay", "Tanauan City", "Taysan", "Tingloy", "Tuy"]
        self.place_weights = [
            3 if place == "Tanauan" else 5 if place == "Laurel" else 1 for place in self.places]
        self.educ_level = [0, 1, 2, 3, 4, 5, 6, 7]
        self.educ_level_weights = [
            [0.001, 0.105, 0.272, 0.282, 0.205, 0.170, 0.144, 0.001],  # 18-24
            [0.012, 0.177, 0.133, 0.124, 0.293, 0.110, 0.133, 0.018],  # 25-34
            [0.008, 0.132, 0.188, 0.274, 0.150, 0.082, 0.154, 0.012],  # 35-44
            [0.024, 0.202, 0.198, 0.230, 0.268, 0.032, 0.038, 0.008],  # 45-54
            [0.188, 0.202, 0.245, 0.130, 0.181, 0.028, 0.022, 0.004],  # 55-64
            [0.302, 0.278, 0.223, 0.080, 0.082, 0.020, 0.013, 0.002]   # 65+
        ]
        self.types = self.get_types()
        self.data = self.generate_data(n)

    def get_types(self):
        arr = []
        with open("answers.csv", "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                s = line.strip().split(";")
                arr.append(s[1])
        return arr

    def generate_education_level(self, age):
        age_index = None
        for i, age_range in enumerate(self.age_range):
            if age <= age_range:
                age_index = i
                break

        if age_index is None:
            # Default to the last age range if age is greater than the maximum
            age_index = len(self.age_range) - 1

        probabilities_for_age = self.educ_level_weights[age_index]
        education_level = rd.choices(
            self.educ_level, probabilities_for_age)[0]
        return education_level

    def generate_data(self, n):
        arr = []
        for _ in range(n):
            a1 = rd.choices(self.age_range, weights=(
                50, 20, 12, 8, 7, 3), k=1)[0]
            a2 = rd.choices(self.gender, weights=(10, 44, 46), k=1)[0]
            a3 = rd.choices(self.places, weights=self.place_weights)[0]
            a4 = ""
            a5 = self.generate_education_level(a1)
            a6 = rd.choices([0, 1], weights=(30, 70))[0]
            a7 = rd.choices([0, 1, 2, 3, 4, 5], weights=[
                            32, 25, 20, 18, 4, 1])[0]
            a8 = set(rd.choices([0, 1, 2, 3, 4, 5], k=rd.randint(1, 5)))
            a9 = rd.choices(range(1, 8), weights=(10, 15, 30, 20, 15, 8, 2))[0]
            a10 = rd.choices(range(0, 6), weights=(18, 28, 14, 20, 12, 8))[0]
            a11 = rd.choices(range(0, 6), weights=(18, 28, 14, 12, 20, 8))[0]
            a12 = rd.choices(range(5), weights=(60, 5, 15, 18, 2))[0]

            # section 2
            a13 = rd.choices(range(4), weights=(5, 5, 10, 5))[0]
            a14 = rd.choices(range(4), weights=(20, 10, 5, 2))[0]
            a15 = rd.choices(range(4), weights=(20, 10, 5, 2))[0]
            a16 = set(rd.choices(range(5), weights=(20, 10, 0, 2, 2), k=2))
            a17 = rd.choices([0, 1], weights=(70, 30))[0]
            a18 = rd.choices(range(3), weights=(20, 10, 0))[0]
            a19 = rd.choices([0, 1], weights=(55, 45))[0]
            a20 = set(rd.choices(range(4), weights=(
                20, 10, 5, 5), k=rd.randint(1, 4)))
            a21 = rd.choices(range(4), weights=(40, 18, 12, 1))[0]
            a22 = rd.choices([0, 1], weights=(70, 30))[0]
            a23 = rd.choices([0, 1], weights=(20, 80))[0]
            a24 = rd.choices([0, 1], weights=(55, 45))[0]
            a25 = set(rd.choices(range(5), k=rd.randint(1, 5)))
            a26 = rd.choices([0, 1], weights=(70, 30))[0]

            # section 3
            a27 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a28 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a29 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a30 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a31 = rd.choices(range(5), weights=(18, 22, 40, 14, 6))[0]
            a32 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a33 = rd.choices(range(5), weights=(60, 17, 13, 9, 1))[0]
            a34 = rd.choices(range(5), weights=(18, 14, 22, 40, 6))[0]
            a35 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a36 = rd.choices(range(5), weights=(40, 22, 18, 14, 6))[0]
            a37 = rd.choices(range(5), weights=(60, 17, 13, 9, 1))[0]

            # section 4
            a38 = rd.choices(range(4), weights=(21, 21, 37, 21))[0]
            a39 = rd.choices(range(4), weights=(21, 21, 37, 21))[0]
            a40 = rd.choices(range(4), weights=(21, 37, 21, 21))[0]
            a41 = rd.choices(range(4), weights=(21, 21, 37, 21))[0]
            a42 = rd.choices(range(4), weights=(20, 20, 23, 37))[0]
            a43 = rd.choices(range(4), weights=(37, 21, 23, 21))[0]
            a44 = rd.choices(range(4), weights=(20, 35, 25, 20))[0]
            a45 = rd.choices(range(4), weights=(20, 20, 23, 37))[0]
            a46 = rd.choices(range(4), weights=(20, 23, 37, 20))[0]
            a47 = rd.choices(range(4), weights=(20, 23, 37, 20))[0]
            a48 = rd.choices(range(4), weights=(20, 37, 23, 20))[0]
            a49 = rd.choices(range(4), weights=(22, 18, 23, 37))[0]

            arr.append([(self.types[i], value) for i, value in enumerate([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20,
                                                                          a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49])])

        return arr


def main():
    data = Data(2).data
    print(data)


if __name__ == "__main__":
    main()
