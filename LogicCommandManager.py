from Heart.Commands.Client.PurchaseOfferCommand import PurchaseOfferCommand
from Heart.Commands.Server.ChangeAvatarNameCommand import ChangeAvatarNameCommand
from Heart.Commands.Client.SetPlayerThumbnailCommand import SetPlayerThumbnailCommand
from Heart.Commands.Client.SetPlayerNameColorCommand import SetPlayerNameColorCommand

class LogicCommandManager:
    commandsList = {
        201: ChangeAvatarNameCommand,
        505: SetPlayerThumbnailCommand,
        527: SetPlayerNameColorCommand,
        519: PurchaseOfferCommand,  # 🔥 PurchaseOfferCommand
        # остальные команды можно оставить как строки
    }

    @staticmethod
    def getCommandsName(commandType):
        command = LogicCommandManager.commandsList.get(commandType, str(commandType))
        return command if isinstance(command, str) else command.__name__

    @staticmethod
    def commandExist(commandType):
        return commandType in LogicCommandManager.commandsList

    @staticmethod
    def createCommand(commandType, commandPayload=None):
        if not LogicCommandManager.commandExist(commandType):
            print(commandType, "skipped")
            return None

        cmd_class = LogicCommandManager.commandsList[commandType]
        cmd_name = LogicCommandManager.getCommandsName(commandType)
        print(f"{cmd_name} created")

        if isinstance(cmd_class, str):
            return None

        # 🔥 Если payload пустой — создаём пустой буфер
        if commandPayload is None:
            commandPayload = b''

        return cmd_class(commandPayload)

    @staticmethod
    def isServerToClient(commandType):
        if 200 <= commandType < 500:
            return True
        elif commandType >= 500:
            return False
