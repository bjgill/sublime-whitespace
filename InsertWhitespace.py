import sublime, sublime_plugin

class InsertWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Separate out regions to cope with multiple selections
        for region in self.view.sel():

            # get full lines
            lines = self.view.substr(self.view.line(region)).split("\n")
            new_lines = []

            for line in lines:
                new_line = line
                if len(line) < 79:
                    # If a line is shorter than 79 characters, append spaces
                    new_line += " " * (79 - len(line))
                new_lines.append(new_line)

            self.view.replace(edit, region, "\n".join(new_lines))
