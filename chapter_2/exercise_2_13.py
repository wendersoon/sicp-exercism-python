"""
When the percentage tolerances are small, the tolerance of the product of two intervals is approximately the sum of the factor tolerances.

function1 and function2 produce different results because interval arithmetic loses the dependencies between variables when they appear more than once, causing one method to generate wider intervals than the other.

"""