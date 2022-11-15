import numpy as np
from sympy import solve, Eq, sympify, diff
from sympy.abc import y, x


class TwoLines:
    def __init__(self, eq_str1, eq_str2, x_points, x_min, x_max):
        # converts the string into a solvable equation.
        # check if y list is empty (no equations has been entered)
        if eq_str1 != '':
            expr1 = sympify(eq_str1)
            self.eq_1_ne, self.eq_1 = expr1, Eq(expr1, y)
        elif eq_str1 == '':
            self.eq_1, self.eq_1_ne = None, None

        if eq_str2 != '':
            expr2 = sympify(eq_str2)
            self.eq_2_ne, self.eq_2 = expr2, Eq(expr2, y)
        elif eq_str2 == '':
            self.eq_2, self.eq_2_ne = None, None

        self.x_list = np.linspace(x_min, x_max, x_points)

    def get_intersect(self):
        # solve for both equations, resulting in intercept coordination's if an intercept is present.
        # results will be converted to float in the 'try' statement if an intercept is present.
        # result_float when two intercept coordination: [[x, y], [x, y]].
        # if one intersect is present, Solve wil result in a dictionary.
        try:
            result = solve([self.eq_1, self.eq_2], (x, y))
        except AttributeError:
            return 'No intersect'

        if type(result) == list:
            result_float = []
            for i in result:
                nested_float = []
                for j in i:
                    try:
                        nested_float.append(float(j))
                    except TypeError:
                        pass

                if len(nested_float) != 0:
                    result_float.append(nested_float)
                else:
                    pass

            if len(result_float) == 0:
                return 'No intersect'
            else:
                return result_float

        elif type(result) == dict:
            result_one_is = list(result.values())
            if len(result_one_is) == 2:
                return [result_one_is]
            else:
                return 'No intersect'

    def get_x(self):
        return self.x_list

    def get_y(self):
        # for x, return the y-value of the two equations, result will be listed
        list_get_1 = np.array([])
        list_get_2 = np.array([])

        # check if y list is empty (no equations has been entered)
        if self.eq_1 is not None:
            for i in self.x_list:
                sub_1 = self.eq_1.subs(x, i)
                list_get_1 = np.append(list_get_1, solve(sub_1, y))
        else:
            pass

        if self.eq_2 is not None:
            for i in self.x_list:
                sub_2 = self.eq_2.subs(x, i)
                list_get_2 = np.append(list_get_2, solve(sub_2, y))
        else:
            pass

        return list_get_1, list_get_2

    def get_diff(self, eq=None):
        # calculate the derivative of a line
        list_diff_1 = np.array([])
        list_diff_2 = np.array([])

        if eq == 1 and self.eq_1_ne is not None:
            for i in self.x_list:
                df = Eq(diff(sympify(self.eq_1_ne)), y).subs(x, i)
                list_diff_1 = np.append(list_diff_1, solve(df, y))
            return list_diff_1
        else:
            if eq == 2 and self.eq_2_ne is not None:
                for i in self.x_list:
                    df = Eq(diff(sympify(self.eq_2_ne)), y).subs(x, i)
                    list_diff_2 = np.append(list_diff_2, solve(df, y))
                return list_diff_2
            else:
                return []
