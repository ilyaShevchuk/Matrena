from DB.MakeDB import delete_DB, Base, engine, post_MFC
from answererControl import AnswererControl, Button
from recordControl import RecordControl

if __name__ == '__main__':
    control = AnswererControl()

    # Запрос пользователя
    dict1 = control.answerForQuery('снилс')
    for answer in dict1:
        print(answer)
    dict1 = control.answerForQuery('Новый паспорт')
    for answer in dict1:
        print(answer)
    dict1 = control.answerForQuery('Получить паспорт')
    for answer in dict1:
        print(answer)
    # # Словарь содержит кнопки с ответами, дети кнопок элементы таблицы со следующей иерархией:
    # Вопрос -> Способ -> Документы, Порядок действий , Ссылка
    # for key in dict1:
    #     print(key)
    #     for method in dict1[key].getChildrens():
    #         print(method.display())
    #         for info in method.getChildrens():
    #             print(info.display(), end=' ')
    #             # тут весь текст
    #             # print(info.getText())
    #             print()
    #     print()
    # # # Получить главное меню словаря кнопок
    # for element in control.getMainMenu().getChildrens():
    #     print(element.display())

    ### Тест записи

    # Создание заглушки бд мфц
    # Base.metadata.create_all(bind=engine)
    # post_MFC()

    # recorder = RecordControl()
    # newDict = recorder.getMFCsDict()
    # MFCButton = newDict.get('МФЦ Адмиралтейского района')
    # recorder.initializeFreeDates(MFCButton)
    # recorder.makeEntry(MFCButton=MFCButton, buttonTime=Button('12:40'), dateButton=Button("2021-09-21"),
    #                    chatID="12", name="Ilya")
    # print(recorder.getInfoAboutRecordByChatID("12"))
