__author__ = 'Gil'

import JackTokenizer

class CompilationEngine:

    def __init__(self, input, output):
        """
        creates a new compilation engine with
        the given input and output.
        """
        self.tokenizer = JackTokenizer.JackTokenizer(input)
        self.parsedRules = []
        self.outputFile = open(output, 'w')

    def writeNonTerminalStart(self, rule):
        self.outputFile.write("<"+rule+">\n")
        self.parsedRules.append(rule)

    def writeNonTerminalEnd(self):
        self.outputFile.write("</"+rule+">\n")
        self.parsedRules.pop()

    def CompileClass(self):
        """
        compiles a complete class.
        """
        token, value = self.tokenizer.advance()
        self.writeNonTerminalStart(token)

    def CompileClassVarDec(self):
        """
        compiles a static declaration or a field
        declaration.
        """
        return

    def CompileSubroutine(self):
        """
        compiles a complete method, function,
        or constructor.
        """
        return

    def compileParameterList(self):
        """
        compiles a (possibly empty) parameter
        list, not including the enclosing “()”.
        """
        return

    def compileVarDec(self):
        """
        compiles a var declaration.
        """
        return

    def compileStatements(self):
        """
        compiles a sequence of statements, not
        including the enclosing “{}”.
        """
        return

    def compileDo(self):
        """
        Compiles a do statement
        """
        return

    def compileLet(self):
        """
        Compiles a let statement
        """
        return

    def compileWhile(self):
        """
        Compiles a while statement
        """
        return

    def compileReturn(self):
        """
        compiles a return statement.
        """
        return

    def compileIf(self):
        """
        compiles an if statement, possibly
        with a trailing else clause.
        """
        return

    def CompileExpression(self):
        """
        compiles an expression.
        """
        return

    def CompileTerm(self):
        """
        compiles a term
        """
        return

