import math
import fractions

def main():
    try:
        print('QUADRACTIC SOLVER: a𝑥² + b𝑥 + c = 0\n')
        int1 = fractions.Fraction(input('Input the co-efficient of 𝑥² term: '))
        int2 = fractions.Fraction(input('Input the coefficient of the 𝑥 term: '))
        int3 = fractions.Fraction(input('Input the constant term: '))

        deqtn = math.sqrt((int2)**2 - 4*(int1)*(int3))

        x1 = (-(int2) + deqtn) / (2*int1)
        x1round = round(x1, 2)

        x2 = (-(int2) - deqtn) / (2*int1)
        x2round = round(x2, 2)

        print('\nThe two roots are: \n X1 = ' + str(x1) + '... which is rounded to: ' + str(x1round) )
        print(' X2 = ' + str(x2) + '... which is rounded to: ' + str(x2round) )
    except ValueError:
        print('\nRoots are non-real.')
    
main()