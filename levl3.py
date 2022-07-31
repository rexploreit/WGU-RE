from sys import exit


class CustomInterpreterPointerError(Exception):
    """ Exception handler for Pointer out of bounds error """

    def __str__(self):
        """alert to pointer being out of bounds"""

        return "POINTER OUT OF BOUNDS"


class CustomInterpreterValueError(Exception):
    """ Exception handler for cell value out of bounds error """

    def __str__(self):
        """alert to a cell being out of bounds"""

        return "INCORRECT VALUE"


class CustomInterpreterSyntaxError(Exception):
    """ Exception handler for pointer out of bounds error """

    def __str__(self):
        """alert to a jump pattern syntax error"""

        return "SYNTAX ERROR"


class CustomInterpreterInputError(Exception):
    """ Exception handler for input being non numerical or out of bounds """

    def __str__(self):
        """alert to input being non-numerical or out of bounds"""

        return "INVALID INPUT"


class CustomInterpreterMissingInputError(Exception):
    """ Exception handler for missing input error """

    def __str__(self):
        """alert to a missing input error"""

        return "MISSING INPUT"


class CustomInterpreter:
    """ Simple custom interpreter class that can parse and execute a given string of commands """

    def __init__(self, s, n):
        """ Object setup creates a list of zero filled cells with a pointer pointing to
        the first cell.  It also has an empty string to be built up as an output and a
        loop dictionary to keep track of our jump indices.  We assume an error on exit
        and only update it to non-error if everything executes properly. """

        self.exit_status = 1
        self.memory = [0] * s
        self.inputs = n
        self.pointer = 0
        self.output = ""
        self.loop_depth = 0
        self.loops = {}

    def execute_command(self, cmd):
        """ Looks over each command and updates our object appropriately """

        if cmd == ">":
            if self.pointer + 1 < len(self.memory):
                self.pointer += 1
            else:
                raise CustomInterpreterPointerError

        if cmd == "<":
            if self.pointer:
                self.pointer -= 1
            else:
                raise CustomInterpreterPointerError

        if cmd == "~":
            if self.memory[self.pointer] < 255:
                self.memory[self.pointer] += 1
            else:
                raise CustomInterpreterValueError

        if cmd == "-":
            if self.memory[self.pointer]:
                self.memory[self.pointer] -= 1
            else:
                raise CustomInterpreterValueError

        if cmd == "&":
            self.output += chr(self.memory[self.pointer])

        if cmd == "|":
            self.inputs.append(self.memory[self.pointer])

        if cmd == "$":
            if self.inputs:
                self.memory[self.pointer] = self.inputs.pop(0)
            else:
                raise CustomInterpreterMissingInputError

    def parse_line(self, line):
        """ Checks command sequence to see if there are any jump instructions
        to be handeled before sending our commands to be executed """

        for jump_position, character in enumerate(line):
            if character == "[":
                self.loops.update({self.loop_depth: [jump_position + 1, None]})
                self.loop_depth += 1

            elif character == "]":
                if self.loop_depth:
                    self.loop_depth -= 1
                    self.loops[self.loop_depth][1] = jump_position

                    start, stop = self.loops[self.loop_depth]
                    new_line = line[start:stop]

                    for _ in range(self.memory[self.pointer]):
                        if "[" in new_line:
                            self.parse_line(new_line)
                        else:
                            for character in new_line:
                                self.execute_command(character)
                else:
                    raise CustomInterpreterSyntaxError

            else:
                self.execute_command(character)

        if self.loop_depth:
            raise CustomInterpreterSyntaxError


if __name__ == "__main__":
    user_input = input("flag > ")

    encoded_algorithm = """
    $[>>~~~~~ ~~~~~ ~~~~~[<~~~~~ ~~~~~ ~~~~~ ~~>-]$[<->-]<|[-]<-] =xx
    $|$|$>>~~~~~ ~~~~- -~[<~~~~~ ~~~~~ ~-=>-]<~~~~- =[<->-]<&[-]| =87
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~-=>-]<----- ~[<->-]<&[-]| =71
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~-=>-]<~~~~~ =[<->-]<&[-]| =85
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~~~>-]<---~~ ~[<->-]<&[-]| =45
    $|$|$>>~~~~~ ~~~~~ =~[<~~~~~ ~~~~~ ~-=>-]<----~ ~[<->-]<&[-]| =76
    $|$|$>>~~~~~ ~~~~~ =~[<~~~~~ ~~~~~ -=~>-]<----~ =[<->-]<&[-]| =69
    $|$|$>>~~~~~ ~~~~~ -~[<~~~~~ ~~~~~ =-~>-]<----= ~[<->-]<&[-]| =86
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ =~->-]<~~~~= -[<->-]<&[-]| =76
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ -=~>-]<~~~~- =[<->-]<&[-]| =45
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~~~>-]<~~~~~ ~[<->-]<&[-]| =48
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~-=>-]<----~ ~[<->-]<&[-]| =48
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~~~>-]<---~~ ~[<->-]<&[-]| =48
    $|$|$>>~~~~~ ~~~~~ ~~[<~~~~~ ~~~~~ ~~~>-]<----- ~[<->-]<&[-]| =51
    """

    try:
        if sum(1 for x in encoded_algorithm if x == "[") != sum(
            1 for x in encoded_algorithm if x == "]"
        ):
            raise CustomInterpreterSyntaxError

        inputs = [len(user_input)]
        for i in range(inputs[0]):
            number = ord(user_input[i])
            if 0 <= number <= 255:
                inputs.append(number)
            else:
                raise CustomInterpreterInputError

        ci = CustomInterpreter(3, inputs)
        ci.parse_line(encoded_algorithm)
        ci.exit_status = 0

        if ci.output != "WGU-LEVL-0003":
            print("please try again")
        else:
            print("You got it. Very well done!!")

    except CustomInterpreterPointerError:
        print(CustomInterpreterPointerError())
    except CustomInterpreterValueError:
        print(CustomInterpreterValueError())
    except CustomInterpreterMissingInputError:
        print(CustomInterpreterMissingInputError())
    except CustomInterpreterSyntaxError:
        print(CustomInterpreterSyntaxError())
    except (ValueError, CustomInterpreterInputError):
        print(CustomInterpreterInputError())
    finally:
        exit(ci.exit_status)
