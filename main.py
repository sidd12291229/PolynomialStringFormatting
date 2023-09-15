def mk_term(coefficient, degree):
    if degree == 0:
        return str(f'+ {coefficient}')
    elif coefficient == 1:
        if not degree == 1:
            return f'x^{degree}'
        else:
            return 'x'
    elif coefficient == -1:
        if not degree == 1:
            return f'-x^{degree}'
        else:
            return '-x'
    else:
        if not degree == 1:
            return f'{coefficient}x^{degree}'
        else:
            return f'{coefficient}x'


def format_poly(coefficients):
    formatted_terms = []

    for degree, coefficient in enumerate(coefficients):

        if coefficient != 0:
            term = mk_term(coefficient, degree)

            if coefficient < 0:
                formatted_terms.append(term)

            else:
                if formatted_terms:
                    formatted_terms.append(f'+ {term}')

                else:
                    formatted_terms.append(term)

    formatted_terms.reverse()

    print(formatted_terms)

    if formatted_terms[0].startswith('+'):
        formatted_terms[0] = formatted_terms[0][1:]

    print(formatted_terms)

    formatted_poly = ' '.join(formatted_terms) if formatted_terms else '0'

    return formatted_poly


def main():
    coefficients = [1,3,2]
    formatted_poly = format_poly(coefficients)
    print(f'\n{formatted_poly}')


if __name__ == '__main__':
    main()
