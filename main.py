from colorama import init, Fore, Back, Style

init(autoreset=True)


# 实现控制台颜色输出类
class Colored(object):

    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.RED + s

    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + s

    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s

    #  前景色:蓝色  背景色:默认
    def blue(self, s):
        return Fore.BLUE + s

    #  前景色:洋红色  背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + s

    #  前景色:青色  背景色:默认
    def cyan(self, s):
        return Fore.CYAN + s

    #  前景色:白色  背景色:默认
    def white(self, s):
        return Fore.WHITE + s

        #  前景色:黑色  背景色:默认

    def black(self, s):
        return Fore.BLACK + s

    #  前景色:白色  背景色:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s

    def dave(self, s):
        return Style.BRIGHT + Fore.GREEN + s


def main():
    color = Colored()
    print(color.green("你好"))


if __name__ == '__main__':
    main()
