import PolynomualCalculation as pom


if __name__ == "__main__":
    poly1 = pom.Polynomial({8 : 1,2 : 1,3 : 5,0: 8})
    poly2 = pom.Polynomial({5 : 1,3 : 1,4 : 5,0: 8})
    constant_1 = 4
    constant_2 = -3

    result_add1 = poly1 + poly2
    result_add2 = constant_1 + poly2
    result_add3 = constant_1 + constant_1
    result_sub1 =  poly1 - poly2
    result_sub2 = poly1 - constant_1
    result_sub3 = constant_1 - poly1
    result_sub4 = constant_1 - constant_2
    result_mul1 = poly1 * poly2
    result_mul2 =  poly2 * 0
    result_pow = poly1 ** 3

    print("Polynomial addition:",result_add1)
    print("Adding constants and polynomials:", result_add2)
    print("Constant addition:", result_add3)
    print("Polynomial Subtraction:", result_sub1)
    print("Polynomial minus constant:", result_sub2)
    print("Constant minus polynomial:", result_sub3)
    print("Constant subtraction:", result_sub4)
    print("Multiplying Polynomials:", result_mul1)
    print("Multiplying a polynomial by a constant:", result_mul2)
    print("Power of Polynomial:", result_pow)
