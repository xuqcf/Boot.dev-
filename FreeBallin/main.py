def create_pipeline(step_one):
    def with_step_two(step_two): #first function, returns step two
        def with_option(option=None): #inner function, returns option
            def inner_most(text): #inner most function (main logic)
                if option == "--one":
                    return step_one(text)
                elif option == "--two":
                    return step_two(text)
                elif option == "--both" or option is None:
                    return step_two(step_one(text))
                else:
                    raise Exception("invalid option")
            return inner_most
        return with_option
    return with_step_two 