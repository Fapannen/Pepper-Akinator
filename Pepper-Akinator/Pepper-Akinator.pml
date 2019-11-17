<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Pepper-Akinator" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="Pepper-Akinator_behav" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="StartGame" src="StartGame/StartGame.dlg" />
        <Dialog name="getUserInput" src="getUserInput/getUserInput.dlg" />
    </Dialogs>
    <Resources>
        <File name="PyPepperAkinator" src="PyPepperAkinator.py" />
        <File name="index" src="html/index.html" />
    </Resources>
    <Topics>
        <Topic name="StartGame_czc" src="StartGame/StartGame_czc.top" topicName="StartGame" language="cs_CZ" />
        <Topic name="getUserInput_czc" src="getUserInput/getUserInput_czc.top" topicName="getUserInput" language="cs_CZ" />
        <Topic name="GallowsGame_czc" src="GallowsGame/GallowsGame_czc.top" topicName="GallowsGame" language="cs_CZ" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_cs_CZ" src="translations/translation_cs_CZ.ts" language="cs_CZ" />
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
