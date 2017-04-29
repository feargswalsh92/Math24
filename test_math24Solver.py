from unittest import TestCase

from Math24 import Math24Solver

<<<<<<< HEAD

class TestMath24Solver(TestCase):
    def test__calculateEquation(self):
        self.assertEqual(Math24Solver._calculateEquation(self,2,"+",3),5)


=======
class TestMath24Solver(TestCase):

    def test__calculateEquation(self):
        s = Math24Solver()

        #addition
        nt = Math24Solver._calculateEquation(s, 2, "+", 3)
        self.assertEqual(nt, 5)

        #subtraction
        nt = Math24Solver._calculateEquation(s, 3, "-", 3)
        self.assertEqual(nt, 0)

        #multiplication
        nt = Math24Solver._calculateEquation(s, 3, "*", 3)
        self.assertEqual(nt, 9)

        #division
        nt = Math24Solver._calculateEquation(s, 12, "/", 3)
        self.assertEqual(nt, 4)

    def test__is24(self):
        s= Math24Solver()
        values=[9,2,2,12]

        #correct answer
        ans = Math24Solver._is24(s ,values, "*","*","-" )
        self.assertEquals(ans, True)

        #incorrect answer
        ans= Math24Solver._is24(s, values, "+","-","+")
        self.assertEquals(ans, False)

    def test__isPlusOrMinus(self):
        s = Math24Solver()
        plus= Math24Solver._isPlusOrMinus(s, "+")
        minus= Math24Solver._isPlusOrMinus(s, "-")
        mult= Math24Solver._isPlusOrMinus(s, "*")
        div= Math24Solver._isPlusOrMinus(s, "/")
        self.assertEquals(plus, True)
        self.assertEquals(minus, True)
        self.assertEquals(mult, False)
        self.assertEquals(div, False)

    def test__formatSolution(self):
        s=Math24Solver()
        values= [10,6,8,3]
        sol=Math24Solver._formatSolution(s,values,"+","-","*")
        self.assertEquals(sol, "(10+6-8)*3")



    def test_solve(self):
        s= Math24Solver()
        values=[9,2,2,12] #solvable
        sol= Math24Solver.solve(s,values)
        self.assertEquals(sol, "9*2*2-12")

        values=[1,3,2,2] #no solution
        sol = Math24Solver.solve(s, values)
        self.assertEquals(sol, "No Solutions")

    #test for exception error in solve method
    def test_solve_less_four_values(self):
        s = Math24Solver()
        values2 = [2, 2, 2]  # too few digits
        with self.assertRaises(ValueError):
            Math24Solver.solve(s, values2)
>>>>>>> d0faee827a1924d25b51982b9ee17d1e46eaf9d0
