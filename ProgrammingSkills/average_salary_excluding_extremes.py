class Solution(object):
    def average(self, salaries):
        """
        :type salary: List[int]
        :rtype: float
        """

        min_salary = 10e6
        max_salary = 1e3

        salary_sum = 0.0

        for salary in salaries:
            if salary < min_salary:
                min_salary = salary

            if salary > max_salary:
                max_salary = salary

            salary_sum += salary

        salary_sum -= min_salary + max_salary

        return salary_sum / (len(salaries) - 2)
