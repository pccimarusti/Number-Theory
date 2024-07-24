import matplotlib.pyplot as plt
import progressbar


def collatz_conjecture():
    def collatz(x):
        collatz_num = 0
        while x != 1:
            # checks if x = 1 (if it is, the function is finished)

            if x % 2 == 1:
                # if x is odd
                x = 3 * x + 1
                collatz_num += 1

            else:
                # if x is even
                x /= 2
                collatz_num += 1

        return collatz_num

    collatz_type_of_computation = input("What would you like to do: \n a) Test range of numbers \n "
                                        "b) Test a single number \n c) Test a python formatted list of numbers \n")

    if collatz_type_of_computation == "a":
        collatz_range_type_of_computation = input("Would you like to \n a) plot \n b) get ordered pairs \n ")
        lower_bound = int(input("Enter a lower bound (inclusive): "))
        upper_bound = int(input("Enter an upper bound (inclusive): ")) + 1

        if collatz_range_type_of_computation == "a":
            x_list = []
            y_list = []
            num_pts = upper_bound - lower_bound
            dpi = 600

            with progressbar.ProgressBar(max_value=num_pts, widgets=[progressbar.Percentage(),
                                                                     progressbar.GranularBar(),
                                                                     progressbar.ETA()]) as bar:
                for i in range(num_pts):
                    x_list.append(lower_bound)
                    y_list.append(collatz(lower_bound))

                    bar.update(i)
                    lower_bound += 1

            plt.rcParams["figure.dpi"] = dpi
            plt.scatter(x_list, y_list, label="circle", color="blue",
                        marker=",", edgecolors=None, s=1)

            plt.show()

            # Max
            y_list.sort()
            y_max = y_list[-1]

            # Mean
            collatz_total = 0
            for y in y_list:
                collatz_total += y
            collatz_mean = collatz_total / len(y_list)

            specs = {"dpi": dpi, "num_pts": num_pts, "highest_pt": y_max, "mean": collatz_mean}
            print(specs)

        elif collatz_range_type_of_computation == "b":
            while lower_bound < upper_bound:
                print("(", lower_bound, ", ", collatz(lower_bound), ")", sep="")
                lower_bound += 1

    elif collatz_type_of_computation == "b":
        num = int(input("Enter a number: "))
        print("(", num, ", ", collatz(num), ")", sep="")

    elif collatz_type_of_computation == "c":
        lst = input("Enter a list: ")
        final_list = eval(lst)
        for ele_num in range(0, len(final_list)):
            ele = final_list[ele_num]
            print("(", ele, ", ", collatz(ele), ")", sep="")

    else:
        print("Please enter a valid input next time...")


def pythagorean_triples():
    def test_pythagorean(pythagorean_lst):

        hypotenuse = max(pythagorean_lst)
        pythagorean_lst.remove(hypotenuse)
        pythagorean_lst.insert(0, hypotenuse)
        # Removed the hypotenuse length and places it at the beginning of the list

        if pythagorean_lst[0] ** 2 == float(pythagorean_lst[1] ** 2) + float(pythagorean_lst[2] ** 2):
            return True
        else:
            return False

    # TERMINATED: Solution: There exists one and only one evenly spaced primitive pythagorean triple: [3, 4, 5]

    # def test_xavier_pythagorean_triples(pythagorean_triple):
    #     if pythagorean_triple[2] == pythagorean_triple[0] + 2:
    #         print(2*(math.sqrt((pythagorean_triple[2]+pythagorean_triple[0])/2)))
    #         if float(pythagorean_triple[1]) == float(2*(math.sqrt((pythagorean_triple[2]+pythagorean_triple[0])/2))):
    #             return True
    #     else:
    #         return False

    def generate_pythagorean_triples():
        # Euclid's formula
        generated_list_pythagorean_triples = []
        for k in range(2, 1000):
            n = 1
            m = 2 * k + 1

            a = (m ** 2 - n ** 2)
            b = (2 * m * n)
            c = (m ** 2 + n ** 2)
            generated_pythagorean_triple = [a, b, c]
            generated_list_pythagorean_triples.append(generated_pythagorean_triple)
        return generated_list_pythagorean_triples

    pythagorean_type_of_computation = input("What would you like to do: \n a) Test Triplets \n "
                                            "b) Generate Triplets (with Euclid's formula) \n "
                                            "NOTE* the test_xavier_pythagorean_triples project has been terminated "
                                            "with single primitive solution [3, 4, 5] \n")
    if pythagorean_type_of_computation == "a":
        pythagorean_triplets_test_list = input("Please enter the triplet you would like to test: \n")
        print(test_pythagorean(eval(pythagorean_triplets_test_list)))
    if pythagorean_type_of_computation == "b":
        print(generate_pythagorean_triples())
    else:
        print("Please enter a valid input next time.")


def primes():
    def get_primes_by_sudo_factors(lower_bound, upper_bound):
        primes_lst = []
        for n in range(lower_bound, upper_bound + 1):
            # + 1 allows the range to be inclusive
            sudo_factors = 0
            for j in range(2, n // 2 + 1):
                if n % j == 0:
                    sudo_factors += 1
            if sudo_factors == 0:
                primes_lst.append(n)

        return primes_lst

    def test_prime(possible_prime):
        for n in range(2, possible_prime // 2 + 1):
            if possible_prime % n == 0:
                return False
        return True

    def test_list_primes(list_possible_primes):
        for i in range(0, len(list_possible_primes) - 1):
            if test_prime(list_possible_primes[i]):
                pass
            else:
                return str(list_possible_primes[i], "is the first non-primitive element.")
            return "all elements are primitive"

    # TERMINATED: No significant result
    # def get_func_primes():
    #     func_primes_lst = []
    #     for n in range(2, 1000):
    #         f = (((math.factorial(n)) % (n + 1)) // n) * (n - 1) + 2
    #         func_primes_lst.append(f)
    #
    #     return func_primes_lst
    #
    # def get_two_indexes():
    #     fp = get_func_primes()
    #     twos = []
    #     for integer in range(len(fp)-1):
    #         if fp[integer] == 2:
    #             twos.append(integer)
    #
    #     return twos

    # def get_num_repeated_twos():
    #     repeated_twos = []
    #     twos_indexes = get_two_indexes()
    #     for index in range(len(twos_indexes) - 1):
    #         a = twos_indexes[index] - index
    #         repeated_twos.append(a)
    #
    #     for x in range(167):
    #         count = 0
    #         for ele in repeated_twos:
    #             if ele == x:
    #                 count += 1
    #
    #         if count >= 1:
    #             print(count, end=", ")
    #
    # def remove_twos():
    #     fp = get_func_primes()
    #     print(fp)
    #     print(len(fp))
    #     # for i in range(len(fp)//2):
    #     #     print(i)
    #     #     if fp[i] == 2:
    #     #         fp.pop(i)
    #     #
    #     # print(fp)

    def goldbach_conjecture(goldbach_natural_number):
        # Every ("even number"?) N > 2 two can be expressed as a sum of primes.
        if goldbach_natural_number % 2 != 0:
            even_continue = input("This is not an even integer, do you wish to continue? y/n \n")
            if even_continue == "n":
                return "Ok."
            elif even_continue == "y":
                pass
            else:
                return "That is not a valid choice. Please try again"

        for number in range(1, goldbach_natural_number):
            goldbach_possible_prime = goldbach_natural_number - number
            print(goldbach_possible_prime, " ", number, ": ", test_prime(goldbach_possible_prime), " ",
                  test_prime(number), sep="")
            if test_prime(goldbach_possible_prime) & test_prime(number):
                return number, goldbach_natural_number - number
        return "This number cannot be expressed as a sum of primes."

    def goldbach_conjecture_range(lower_bound, upper_bound):
        while lower_bound < upper_bound:
            print(lower_bound, ": ", goldbach_conjecture(lower_bound), sep="")
            lower_bound += 2

    def recip_primes():
        def get_recip_period(n):
            r = 1
            r_list = []
            zero_factor = 0
            zero_factors = 0

            while True:
                # print(r, r_list)

                lc = 0
                while r < n:
                    # print(zero_factors)
                    r = r * 10

                    lc += 1
                    # print(lc)
                if lc > 1:
                    zero_factor = lc - 1

                r = r % n
                if r_list.count(r):
                    return len(r_list) + zero_factors
                else:
                    r_list.append(r)
                    r = r % n
                    zero_factors += zero_factor
                    zero_factor = 0

        primes_choice_d_1 = input("What would you like to test for? \n a) Range \n b) Value \n")
        if primes_choice_d_1 == "a":
            recip_primes_computation_type = input("Would you like to \n a) plot \n b) get ordered pairs \n")
            recip_primes_lower_bound = int(input("Enter a lower bound (inclusive): "))
            recip_primes_upper_bound = int(input("Enter an upper bound (inclusive): "))

            recip_primes_domain = get_primes_by_sudo_factors(recip_primes_lower_bound, recip_primes_upper_bound)

            if recip_primes_computation_type == "a":
                recip_primes_x_list = recip_primes_domain
                recip_primes_y_list = []

                num_pts = len(recip_primes_x_list)
                dpi = 600

                with progressbar.ProgressBar(max_value=num_pts, widgets=[progressbar.Percentage(),
                                                                         progressbar.GranularBar()]) as bar:

                    for i in range(len(recip_primes_x_list)):
                        recip_primes_y_list.append(get_recip_period(recip_primes_x_list[i]))
                        bar.update(i)

                print(recip_primes_x_list, "\n", len(recip_primes_x_list), "\n", recip_primes_y_list, "\n",
                      len(recip_primes_y_list))
                plt.rcParams["figure.dpi"] = dpi
                plt.scatter(recip_primes_x_list, recip_primes_y_list, s=1, marker=",")
                plt.show()

            elif recip_primes_computation_type == "b":
                for i in recip_primes_domain:
                    print("(", i, ", ", get_recip_period(i), ")", sep="")
        elif primes_choice_d_1 == "b":
            recip_primes_value = int(input("Enter the value ou would like to test: "))
            print(get_recip_period(recip_primes_value))

    primes_choice = input("What would you like to see? \n a) Generate Primes \n "
                          "b) Test for Prime \n c) Test Goldbach Conjecture \n "
                          "d) Find period of reciprocals of primes \n")
    if primes_choice == "a":
        print(get_primes_by_sudo_factors(int(input("Enter a lower bound to generate from (inclusive): ")),
                                         int(input("Enter an upper bound to generate to (inclusive): "))))

    elif primes_choice == "b":
        primes_choice_b_1 = input("Test for: \n a) value \n b) list \n")

        if primes_choice_b_1 == "a":
            print(test_prime(int(input("Enter the number you would like to test: "))))
        elif primes_choice_b_1 == "b":
            list_of_possible_primes = input("Please enter a list: ")
            print(test_list_primes(eval(list_of_possible_primes)))

    elif primes_choice == "c":
        goldbach_choice = input("Would you like to test a) a value, or b) a range of values? \n")
        if goldbach_choice == "a":
            print(goldbach_conjecture(int(input("Enter the number you would like to test: "))))
        elif goldbach_choice == "b":
            goldbach_lower_bound = int(input("Enter the lower bound of the range you would like to test: "))
            goldbach_upper_bound = int(input("Enter the lower bound of the range you would like to test: "))
            goldbach_conjecture_range(goldbach_lower_bound, goldbach_upper_bound)
    elif primes_choice == "d":
        recip_primes()


main_input = input("What would you like to see? \n a) Collatz \n b) pythagorean_triples \n c) primes \n")
if main_input == "a":
    collatz_conjecture()
elif main_input == "b":
    pythagorean_triples()
elif main_input == "c":
    primes()
