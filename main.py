from sec_class import Secretary
from sec_data import documents, directories, command_help

app = Secretary(documents, directories, command_help)
app.main()
