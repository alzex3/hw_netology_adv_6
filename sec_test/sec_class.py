class Secretary:
    def __init__(self, _docs, _dirs, _help):
        self._docs = _docs.copy()
        self._dirs = _dirs.copy()
        self._help = _help

    def main(self):
        print('Программа "Виртуальный секретарь" запущена!')
        print('Для получения справки введите "help"')
        while True:
            command = input('\nВведите команду: ')
            if command == 'p':
                num = (input('Введите номер документа: '))
                print(self.get_people(num))
            elif command == 's':
                num = input('Введите номер документа: ')
                print(self.get_shelf(num))
            elif command == 'l':
                print('Список всех документов:')
                print(self.get_list())
            elif command == 'a':
                doc_type = input('Введите тип документа:\n')
                doc_num = input('Введите номер документа:\n')
                doc_name = input('Введите имя владельца:\n')
                doc_shelf = input('Введите номер полки хранения:\n')
                self.add(doc_type, doc_num, doc_name, doc_shelf)
            elif command == 'd':
                num = (input('Введите номер документа который необходимо удалить: '))
                self.delete(num)
            elif command == 'm':
                num = (input('Введите номер документа который необходимо переместить: '))
                shelf = (input('Введите номер полки на которую необходимо переместить документ: '))
                self.move(num, shelf)
            elif command == 'as':
                shelf = (input('Введите номер полки которую необходимо добавить: '))
                self.add_shelf(shelf)
            elif command == 'help':
                print(self._help)
            elif command == 'exit':
                print('Программа завершена!')
                return
            else:
                print('Комманда введена неверно, повторите ввод!')

    def is_num_exist(self, num):
        for doc in self._docs:
            if num == doc.get('number'):
                return True
        return False

    def get_people(self, doc_num):
        if self.is_num_exist(doc_num):
            for doc in self._docs:
                if doc_num == doc.get('number'):
                    return doc.get('name')
        else:
            return 'Документа с таким номером не существует!'

    def get_shelf(self, doc_num):
        if self.is_num_exist(doc_num):
            for shelf, doc_nums in self._dirs.items():
                if doc_num in doc_nums:
                    return shelf
        else:
            return 'Документа с таким номером не существует!'

    def get_list(self):
        string = ''
        for doc in self._docs:
            for value in doc.values():
                string += ' ' + f'"{value}"'
            string += '\n'
        return string

    def add(self, doc_type, doc_num, doc_name, doc_shelf):
        if doc_shelf in self._dirs.keys():
            self._docs.append({"type": doc_type, "number": doc_num, "name": doc_name})
            for shelf, doc_nums in self._dirs.items():
                if shelf == doc_shelf:
                    doc_nums.append(doc_num)
        else:
            print('Введённой вами полки не существует!')

    def delete(self, doc_num):
        if self.is_num_exist(doc_num):

            for i, doc in enumerate(self._docs):
                if doc_num in doc.values():
                    del self._docs[i]

            for doc_nums in self._dirs.values():
                for i, num in enumerate(doc_nums):
                    if doc_num == num:
                        doc_nums.pop(i)
        else:
            print('Документа с таким номером не существует!')

    def move(self, doc_num, doc_shelf):
        if self.is_num_exist(doc_num):

            if doc_shelf in self._dirs.keys():

                for doc_nums in self._dirs.values():
                    for i, num in enumerate(doc_nums):
                        if doc_num == num:
                            doc_nums.pop(i)

                for shelf, doc_nums in self._dirs.items():
                    if shelf == doc_shelf:
                        doc_nums.append(doc_num)

            else:
                print('Введённой вами полки не существует!')

        else:
            print('Документа с таким номером не существует!')

    def add_shelf(self, new_shelf):
        if new_shelf not in self._dirs.keys():
            self._dirs[new_shelf] = []
        else:
            print('Полка с таким номером уже существует!')
