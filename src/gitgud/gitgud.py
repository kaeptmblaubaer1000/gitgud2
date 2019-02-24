import argparse
import pyfiglet
import sys


class git(object):
    @staticmethod
    def parse_args(cmdname, args):
        parser = argparse.ArgumentParser(description="Have you been told to 'git %s'? Now you can!" % cmdname)
        parser.add_argument("name", metavar="NAME", type=str, nargs="?", default=None,
                            help="who is getting %s" % cmdname)
        parser.add_argument("-s", "--super", action="store_true", default=False,
                            help="get super %s" % cmdname)
        args = parser.parse_args(args)
        return args

    @staticmethod
    def fig(text):
        fig = pyfiglet.Figlet()
        return fig.renderText(text)

    def __gud(cls, args):
        args = cls.parse_args("gud", args)
        name = args.name or "You"
        sup = args.super
        text = "{name} {verb} now {qual} gud!".format(name=name,
                                                      verb="is" if args.name else "are",
                                                      qual="super" if sup else "so")
        if sup:
            text = cls.fig(text)
        return text

    def __rekt(cls, args):
        args = cls.parse_args("rekt", args)
        name = args.name or "You"
        sup = args.super
        text = "{name} got {qual}#rekt!".format(name=name,
                                                qual="super " if sup else "")
        if sup:
            text = cls.fig(text)
        return text

    def __spooked(cls, args):
        args = cls.parse_args("spooked", args)
        name = args.name or "You"
        sup = args.super
        text = "{name} got spooked by a scary skeleton!".format(name=name)

        if sup:
            text = cls.fig(text)
        return text

    def __job(cls, args):
        args = cls.parse_args("job", args)
        name = args.name or "You"
        sup = args.super
        text = "{name} got a job in gitting #rekt!".format(name=name)

        if sup:
            text = cls.fig(text)
        return text

    def __money(cls, args):
        args = cls.parse_args("money", args)
        name = args.name or "You"
        sup = args.super
        text = "{name} got money!".format(name=name)

        if sup:
            text = cls.fig(text)
        return text

    def _write(s):
        print(s)

    def _make_command(name, handler, *, _write=_write):
        def command(cls, args=None, output=_write):
            output(handler(cls, args))
        return classmethod(command)

    gud = _make_command("gud", __gud)
    rekt = _make_command("rekt", __rekt)
    spooked = _make_command("spooked", __spooked)
    job = _make_command("job", __job)
    money = _make_command("money", __money)
