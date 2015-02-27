__author__ = 'pierre.pichot'


class Table:
    DEFAULT_HEADER_TOP_LEFT = "┍"
    DEFAULT_HEADER_TOP_SEPARATOR = "┯"
    DEFAULT_HEADER_TOP_RIGHT = "┑"
    DEFAULT_HEADER_TOP_LINE_ITEM = "━"
    DEFAULT_HEADER_BOTTOM_LEFT = "┝"
    DEFAULT_HEADER_BOTTOM_SEPARATOR = "┿"
    DEFAULT_HEADER_BOTTOM_RIGHT = "┥"
    DEFAULT_HEADER_BOTTOM_LINE_ITEM = "━"
    DEFAULT_SEPARATOR_LINE_LEFT = "├"
    DEFAULT_SEPARATOR_LINE_SEPARATOR = "┼"
    DEFAULT_SEPARATOR_LINE_RIGHT = "┤"
    DEFAULT_SEPARATOR_LINE_ITEM = "─"
    DEFAULT_BOTTOM_LINE_LEFT = "└"
    DEFAULT_BOTTOM_LINE_SEPARATOR = "┴"
    DEFAULT_BOTTOM_LINE_RIGHT = "┘"
    DEFAULT_BOTTOM_LINE_ITEM = "─"
    DEFAULT_VERTICAL_BORDER = "│"
    DEFAULT_VERTICAL_SEPARATOR = "│"
    CHAR_HEADER_TOP_LEFT = "+"
    CHAR_HEADER_TOP_SEPARATOR = "+"
    CHAR_HEADER_TOP_RIGHT = "+"
    CHAR_HEADER_TOP_LINE_ITEM = "="
    CHAR_HEADER_BOTTOM_LEFT = "+"
    CHAR_HEADER_BOTTOM_SEPARATOR = "+"
    CHAR_HEADER_BOTTOM_RIGHT = "+"
    CHAR_HEADER_BOTTOM_LINE_ITEM = "="
    CHAR_SEPARATOR_LINE_LEFT = "+"
    CHAR_SEPARATOR_LINE_SEPARATOR = "+"
    CHAR_SEPARATOR_LINE_RIGHT = "+"
    CHAR_SEPARATOR_LINE_ITEM = "-"
    CHAR_BOTTOM_LINE_LEFT = "+"
    CHAR_BOTTOM_LINE_SEPARATOR = "+"
    CHAR_BOTTOM_LINE_RIGHT = "+"
    CHAR_BOTTOM_LINE_ITEM = "-"
    CHAR_VERTICAL_BORDER = "|"
    CHAR_VERTICAL_SEPARATOR = "|"
    BORDER_SLICK = "slick"
    BORDER_CHARS = "chars"
    RETURN = "\n"

    # public
    def __init__(
            self,
            columns,
            border_type=BORDER_SLICK):
        """ Inits a new Table object.
            columns: mandatory parameter, set of tuples (column header, size)
            border_type: optional parameter, can be Table.BORDER_SLICK or
            Table.BORDER_CHARS. By default Table.BORDER_SLICK is used
        """
        self.columns = columns
        self.rows = []
        self.totalRowsForHeaders = 1
        self.totalColumns = len(columns)
        self.columnsWidths = []
        self.rows = []
        self.rowsHeights = []
        self.isBorders = True
        self.headerTopLeft = ""
        self.headerTopSeparator = ""
        self.headerTopRight = ""
        self.headerTopLineItem = ""
        self.headerBottomLeft = ""
        self.headerBottomSeparator = ""
        self.headerBottomRight = ""
        self.headerBottomLineItem = ""
        self.separatorLineLeft = ""
        self.separatorLineSeparator = ""
        self.separatorLineRight = ""
        self.separatorLineItem = ""
        self.bottomLineLeft = ""
        self.bottomLineSeparator = ""
        self.bottomLineRight = ""
        self.bottomLineItem = ""
        self.verticalBorder = ""
        self.verticalSeparator = ""
        self.separatorLine = ""
        self.headerTopLine = ""
        self.headerBottomLine = ""
        self.bottomLine = ""
        self.borderType = ""
        self.totalRowsForHeader = 0
        self.headers = []
        self.set_border_type(border_type)
        self._make_header()

    # public
    def set_border_type(self, border_type):
        """ Sets the type of border.
            border_type: mandatory parameter, can be Table.BORDER_SLICK or Table.BORDER_CHARS.
        """
        self.borderType = border_type
        if self.borderType == self.BORDER_SLICK:
            self.have_slick_borders()
        elif self.borderType == self.BORDER_CHARS:
            self.have_chars_borders()
        else:
            print("Wrong border type")  # todo add exception

    # public
    def have_slick_borders(self):
        """ Sets the type of border as Slick (based on UTF-8 characters)."""
        self.set_border_for_header_top(self.DEFAULT_HEADER_TOP_LINE_ITEM,
                                       self.DEFAULT_HEADER_TOP_SEPARATOR,
                                       self.DEFAULT_HEADER_TOP_LEFT,
                                       self.DEFAULT_HEADER_TOP_RIGHT)
        self.set_border_for_header_bottom(self.DEFAULT_HEADER_BOTTOM_LINE_ITEM,
                                          self.DEFAULT_HEADER_BOTTOM_SEPARATOR,
                                          self.DEFAULT_HEADER_BOTTOM_LEFT,
                                          self.DEFAULT_HEADER_BOTTOM_RIGHT)
        self.set_border_for_separator(self.DEFAULT_SEPARATOR_LINE_ITEM,
                                      self.DEFAULT_SEPARATOR_LINE_SEPARATOR,
                                      self.DEFAULT_SEPARATOR_LINE_LEFT,
                                      self.DEFAULT_SEPARATOR_LINE_RIGHT)
        self.set_border_for_footer(self.DEFAULT_BOTTOM_LINE_ITEM,
                                   self.DEFAULT_BOTTOM_LINE_SEPARATOR,
                                   self.DEFAULT_BOTTOM_LINE_LEFT,
                                   self.DEFAULT_BOTTOM_LINE_RIGHT)
        self.set_vertical_borders(
            self.DEFAULT_VERTICAL_SEPARATOR,
            self.DEFAULT_VERTICAL_BORDER)

    # public
    def have_chars_borders(self):
        """ Sets the type of border as Chars (maximum compatibility)."""
        self.set_border_for_header_top(self.CHAR_HEADER_TOP_LINE_ITEM,
                                       self.CHAR_HEADER_TOP_SEPARATOR,
                                       self.CHAR_HEADER_TOP_LEFT,
                                       self.CHAR_HEADER_TOP_RIGHT)
        self.set_border_for_header_bottom(self.CHAR_HEADER_BOTTOM_LINE_ITEM,
                                          self.CHAR_HEADER_BOTTOM_SEPARATOR,
                                          self.CHAR_HEADER_BOTTOM_LEFT,
                                          self.CHAR_HEADER_BOTTOM_RIGHT)
        self.set_border_for_separator(self.CHAR_SEPARATOR_LINE_ITEM,
                                      self.CHAR_SEPARATOR_LINE_SEPARATOR,
                                      self.CHAR_SEPARATOR_LINE_LEFT,
                                      self.CHAR_SEPARATOR_LINE_RIGHT)
        self.set_border_for_footer(self.CHAR_BOTTOM_LINE_ITEM,
                                   self.CHAR_BOTTOM_LINE_SEPARATOR,
                                   self.CHAR_BOTTOM_LINE_LEFT,
                                   self.CHAR_BOTTOM_LINE_RIGHT)
        self.set_vertical_borders(self.CHAR_VERTICAL_SEPARATOR, self.CHAR_VERTICAL_BORDER)

    # public
    def set_border_for_header_top(self, line, separator, left_corner, right_corner):
        """ Sets the border elements for the header's top line.
            line: mandatory parameter: character defining the line element
            separator: mandatory parameter: character defining the line/cell junction element
            left_corner: mandatory parameter: character defining the left hand corner element
            right_corner: mandatory parameter: character defining the right hand corner element
        """
        self.headerTopLeft = left_corner
        self.headerTopSeparator = separator
        self.headerTopRight = right_corner
        self.headerTopLineItem = line

    # public
    def set_border_for_header_bottom(self, line, separator, left_corner, right_corner):
        """ Sets the border elements for the header's bottom line.
            line: mandatory parameter: character defining the line element
            separator: mandatory parameter: character defining the line/cell junction element
            left_corner: mandatory parameter: character defining the left hand corner element
            right_corner: mandatory parameter: character defining the right hand corner element
        """
        self.headerBottomLeft = left_corner
        self.headerBottomSeparator = separator
        self.headerBottomRight = right_corner
        self.headerBottomLineItem = line

    # public
    def set_border_for_separator(self, line, separator, left_corner, right_corner):
        """ Sets the border elements for the table's inner separator line.
            line: mandatory parameter: character defining the line element
            separator: mandatory parameter: character defining the line/cell junction element
            left_corner: mandatory parameter: character defining the left hand corner element
            right_corner: mandatory parameter: character defining the right hand corner element
        """
        self.separatorLineLeft = left_corner
        self.separatorLineSeparator = separator
        self.separatorLineRight = right_corner
        self.separatorLineItem = line

    # public
    def set_border_for_footer(self, line, separator, left_corner, right_corner):
        """ Sets the border elements for the table's bottom line.
            line: mandatory parameter: character defining the line element
            separator: mandatory parameter: character defining the line/cell junction element
            left_corner: mandatory parameter: character defining the left hand corner element
            right_corner: mandatory parameter: character defining the right hand corner element
        """
        self.bottomLineLeft = left_corner
        self.bottomLineSeparator = separator
        self.bottomLineRight = right_corner
        self.bottomLineItem = line

    # public
    def set_vertical_borders(self, inside, outside):
        """ Sets the table's vertical border elements.
            inside: mandatory parameter: inner border's vertical element
            outside: mandatory parameter: outer border's vertical element
        """
        self.verticalBorder = outside
        self.verticalSeparator = inside

    # private
    def _make_header(self):
        tmp_headers = []
        for column, width in self.columns:
            self.columnsWidths.append(width)
            tmp_headers.append(column)
        (tmp_headers, self.totalRowsForHeaders) = self._prepare_row(tmp_headers)
        for i in range(0, self.totalRowsForHeaders):
            tmp_row = []
            j = 0
            for column in tmp_headers:
                cell = ""
                if i <= len(column) - 1:
                    cell = column[i]
                tmp_row.append(cell.ljust(self.columnsWidths[j]))
                j += 1
            self.headers.append(tmp_row)

    # private
    def _make_borders(self):
        self.separatorLine = self.separatorLineLeft
        self.headerTopLine = self.headerTopLeft
        self.headerBottomLine = self.headerBottomLeft
        self.bottomLine = self.bottomLineLeft
        i = 1
        for column in self.columnsWidths:
            self.separatorLine += "".ljust(column, self.separatorLineItem)
            self.headerTopLine += "".ljust(column, self.headerTopLineItem)
            self.headerBottomLine += "".ljust(column, self.headerBottomLineItem)
            self.bottomLine += "".ljust(column, self.bottomLineItem)
            if i < self.totalColumns:
                self.separatorLine += self.separatorLineSeparator
                self.headerTopLine += self.headerTopSeparator
                self.headerBottomLine += self.headerBottomSeparator
                self.bottomLine += self.bottomLineSeparator
            else:
                self.separatorLine += self.separatorLineRight
                self.headerTopLine += self.headerTopRight
                self.headerBottomLine += self.headerBottomRight
                self.bottomLine += self.bottomLineRight
            i += 1

    # private
    def _get_cell_height(self, text_length, width):
        height = 0
        floor_value = text_length // width
        if text_length % width > 0:
            floor_value += 1
        if floor_value > height:
            height = floor_value
        return height

    # private
    def _get_row_height(self, row):
        i = 0
        height = 0
        for column in row:
            width = self.columnsWidths[i]
            length = len(column)
            column_height = self._get_cell_height(length, width)
            if column_height > height:
                height = column_height
            i += 1
        return height

    # private
    def _split_string(self, string, length):
        string_length = len(string)
        if string_length <= length:
            return string
        else:
            total_rows_for_header = 1
            to_return = []
            floor_value = string_length // length
            if string_length % length > 0:
                floor_value += 1
            if floor_value > total_rows_for_header:
                self.totalRowsForHeader = floor_value
            for i in range(0, total_rows_for_header):
                to_return.append(string[i * length:i * length + length - 1])
            return to_return

    # private
    def _split_string_for_rows(self, string, length):
        to_return = []
        while string != "":
            to_append = string[0:length]
            return_index = to_append.find(self.RETURN)
            if return_index == -1:
                string = string[length:]
            else:
                to_append = string[0:return_index]
                string = string[return_index + 1:]
            to_return.append(to_append)
        return to_return

    # private
    def _format_string_for_row(self, string, length, rows):
        to_return = []
        for i in range(0, rows):
            to_append = string[0:length]
            return_index = to_append.find(self.RETURN)
            if return_index == -1:
                string = string[length:]
            else:
                to_append = string[0:return_index]
                string = string[return_index + 1:]
                rows += 1
            to_return.append(to_append.ljust(length))
        return to_return

    # private
    def _prepare_row(self, row):
        to_return = []
        highest = 0
        i = 0
        for column in row:
            prepared_row = self._split_string_for_rows(column, self.columnsWidths[i])
            if len(prepared_row) > highest:
                highest = len(prepared_row)
            to_return.append(prepared_row)
            i += 1

        # print(to_return)
        return to_return, highest

    # public
    def add_row(self, row):
        """ Adds a row to the table.
            row: mandatory parameter: set of Strings
        """
        self._add_or_insert_row(row, -1)

    # public
    def insert_row(self, row, pos):
        """ Inserts a row in the table at a defined position.
            row: mandatory parameter: set of Strings
            pos: mandatory parameter: position, starting at 0
        """
        self._add_or_insert_row(row, pos)

    # private
    # pos = -1 means add
    def _add_or_insert_row(self, row, pos):
        (columns, height) = self._prepare_row(row)
        final_row = []
        for i in range(0, height):
            tmp_row = []
            j = 0
            for column in columns:
                cell = ""
                if i <= len(column) - 1:
                    cell = column[i]
                tmp_row.append(cell.ljust(self.columnsWidths[j]))
                j += 1
            final_row.append(tmp_row)
        if pos == -1:
            self.rows.insert(pos, final_row)
            self.rowsHeights.insert(pos, height)
        else:
            self.rows.append(final_row)
            self.rowsHeights.append(height)

    # public
    def delete_row(self, pos):
        """ Deletes a row in the table at a defined position.
            pos: mandatory parameter: position, starting at 0
        """
        self.rows.pop(pos)
        self.rowsHeights.pop(pos)

    # public
    def draw(self):
        """ Draws the table on the standard output."""
        print(self.generate())

    # private
    def generate(self):
        self._make_borders()
        # header
        to_return = self._add_header_top_line()
        to_return += self._generate_row(self.headers)
        to_return += self._add_header_bottom_line()
        # rows
        row_number = 0
        total_row_number = len(self.rows)
        for row in self.rows:
            to_return += self._generate_row(row)
            row_number += 1
            if row_number == total_row_number:
                to_return += self._add_bottom_line()
            else:
                to_return += self._add_separator_line()
        return to_return

    # private
    def _generate_row(self, row):
        to_return = ""
        for sub_row in row:
            line = self._add_vertical_border()
            pos = 1
            for cell in sub_row:
                    line += cell
                    if pos < self.totalColumns:
                        line += self._add_vertical_separator()
                    else:
                        line += self._add_vertical_border()
                    pos += 1
            to_return += line + self.RETURN
        return to_return

    # private
    def _add_vertical_border(self):
        if self.isBorders:
            return self.verticalBorder
        else:
            return ""

    # private
    def _add_vertical_separator(self):
        if self.isBorders:
            return self.verticalSeparator
        else:
            return ""

    # private
    def _add_separator_line(self):
        if self.isBorders:
            return self.separatorLine + self.RETURN
        else:
            return ""

    # private
    def _add_header_top_line(self):
        if self.isBorders:
            return self.headerTopLine + self.RETURN
        else:
            return ""

    # private
    def _add_header_bottom_line(self):
        if self.isBorders:
            return self.headerBottomLine + self.RETURN
        else:
            return ""

    # private
    def _add_bottom_line(self):
        if self.isBorders:
            return self.bottomLine
        else:
            return ""

    # public
    def make_plain_rows(self):
        """ Do not display vertical separators in rows. """
        self.headerTopSeparator = self.headerTopLineItem
        self.headerBottomSeparator = self.headerBottomLineItem
        self.separatorLineSeparator = self.separatorLineItem
        self.bottomLineSeparator = self.bottomLineItem
        self.verticalSeparator = " "

    # public
    def make_plain_columns(self):
        """ Do not display horizontal separators in rows. """
        self.separatorLineLeft = self.verticalSeparator
        self.separatorLineSeparator = self.verticalSeparator
        self.separatorLineRight = self.verticalSeparator
        self.separatorLineItem = " "
        self.verticalBorder = self.verticalSeparator


if __name__ == "__main__":
    table = Table([("Last name", 20), ("First name", 12), ("Date of birth", 14), ("Occupation", 12), ("Country", 14)])
    table.add_row(["Pichot", "Pierre", "19/06/1984", "Project Manager", "A bit here, a bit there, a bit everywhere..."])
    table.add_row(["Pichot-Denes", "Hanga", "30/11/1987", "Dentist", "Romania"])
    table.add_row(["Tison", "Veronique", "11/05/1962", "Chieuse/Fonctionnaire", "France"])
    # table.haveCharsBorders()
    # table.makePlainRows()
    table.draw()
    # table.insert_row(["Tison", "Olivier", "24/01/1970","Chauffeur Poids-lourd", "France"], 2)
    # table.draw()
    # table.deleteRow(1)
    # table.draw()
