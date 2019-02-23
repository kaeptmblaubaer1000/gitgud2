import argparse
import pyfiglet
import sys


class git(object):
    @staticmethod
    def parse_args(cmdname):
        parser = argparse.ArgumentParser(description="Have you been told to 'git %s'? Now you can!" % cmdname)
        parser.add_argument("name", metavar="NAME", type=str, nargs="?", default=None,
                            help="who is getting %s" % cmdname)
        parser.add_argument("-s", "--super", action="store_true", default=False,
                            help="get super %s" % cmdname)
        args = parser.parse_args()
        return args

    @staticmethod
    def fig(text):
        fig = pyfiglet.Figlet()
        return fig.renderText(text)

    @classmethod
    def gud(cls):
        args = cls.parse_args("gud")
        name = args.name or "You"
        sup = args.super
        text = "{name} {verb} now {qual} gud!".format(name=name,
                                                      verb="is" if args.name else "are",
                                                      qual="super" if sup else "so")
        if sup:
            text = cls.fig(text)
        print(text)

    @classmethod
    def rekt(cls):
        args = cls.parse_args("rekt")
        name = args.name or "You"
        sup = args.super
        text = "{name} got {qual}#rekt!".format(name=name,
                                                qual="super " if sup else "")
        if sup:
            text = cls.fig(text)
        print(text)

    @classmethod
    def spooked(cls):
        args = cls.parse_args("spooked")
        name = args.name or "You"
        sup = args.super
        text = "{name} got spooked by a scary skeleton!".format(name=name)

        if sup:
            text = cls.fig(text)
        print(text)

    @classmethod
    def job(cls):
        args = cls.parse_args("job")
        name = args.name or "You"
        sup = args.super
        text = "{name} got a job in gitting #rekt!".format(name=name)

        if sup:
            text = cls.fig(text)
        print(text)

    @classmethod
    def money(cls):
        args = cls.parse_args("money")
        name = args.name or "You"
        sup = args.super
        text = "{name} got money!".format(name=name)

        if sup:
            text = cls.fig(text)
        print(text)
