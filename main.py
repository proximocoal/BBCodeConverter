from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class TableBuilder(App):
    
    def build(self):
        self.window= GridLayout(cols=1)
      
        self.button = Button(text = "Enter text below. Press here to return formatted text", size_hint = (0.1, 0.1),font_size = 10)
        self.button.bind(on_press = self.getText)
        self.window.add_widget(self.button)
        
        self.text_input = TextInput(multiline=True, padding_y = (5, 5), size_hint = (1, 0.7), font_size = 10)
        self.window.add_widget(self.text_input)
        
        return self.window
       
    def formatter(self, unformatted):
        table_st = "[table]"
        table_end = "[/table]"
        header_st = "[td][b]"
        header_end = "[/b][/td]"
        thead_st = "[thead]"
        thead_end = "[/thead]"
        tbody_st = "[tbody]"
        tbody_end = "[tbody]"
        row_st = "[tr]"
        row_end = "[/tr]"
        cell_st = "[td]"
        cell_end = "[/td]"
        cell = " "
        space = "-"
        output = table_st
        unformatted = unformatted.split("\n")
        for ind, line in enumerate(unformatted):
            if ind == 0:
                output += thead_st
            elif ind == 1:
                output += tbody_st
            output += row_st
            for cell in line.split():
                cell = cell.replace(space, " ")
                st = cell_st
                end = cell_end
                if ind == 0:
                    st = header_st
                    end = header_end
                output += st + cell + end
            output += row_end
            if ind == 0:
                output += thead_end
        output += tbody_end + table_end
        return output
    
    def getText(self, event):
        unformatted = self.text_input.text
        self.text_input.text = self.formatter(unformatted)
    

if __name__ == "__main__":
    TableBuilder().run()