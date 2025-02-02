import os
import utils
import shutil

from const import BASE_PATH, BUILD_PATH, STORY_PATH, ANNOUNCER_PATH, ID_PATH, EGO_PATH, NUM_RETRY

# todo: need to fix ego, id, and enemy skills

if __name__ == '__main__':
    # ! temp
    utils.translate_prefix(STORY_PATH, ['content', 'teller', 'title', 'place'], retry=NUM_RETRY, prefix='S')  # story

    # ! local
    utils.translate_prefix(STORY_PATH,
                           ['content', 'teller', 'title', 'place'],
                           retry=NUM_RETRY,
                           prefix='^[0-9]|^P')  # story

    # ! scripting
    utils.translate_prefix(STORY_PATH,
                           ['content', 'teller', 'title', 'place'],
                           retry=NUM_RETRY,
                           prefix='^[^0-9PS]')  # story
    utils.translate(ANNOUNCER_PATH, ['dlg'], retry=NUM_RETRY)  # announcers
    utils.translate(ID_PATH, ['dlg'], retry=NUM_RETRY)  # id dialogue
    utils.translate(EGO_PATH, ['dlg'], retry=NUM_RETRY)  # ego dialogue

    # ! finished
    utils.translate_prefix('.', ['trans'], prefix='testing', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, ['teller', 'dialog'], prefix='AbDlg_', retry=NUM_RETRY)

    # todo: value "title" is sus
    abs_event_values = ['title', 'eventDesc', 'prevDesc', 'behaveDesc', 'successDesc', 'failureDesc']
    utils.translate_prefix(BASE_PATH, values=abs_event_values, prefix='AbEvents.json', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=abs_event_values, prefix='AbEvents-', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=abs_event_values, prefix='AbEvents_', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='AbEventsResultLog', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH,
                           values=['name', 'clue', 'storyList', 'story', 'codeName'],
                           prefix='AbnormalityGuides', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH,
                           values=['name', 'subDesc', 'desc', 'options', 'message', 'messageDesc', 'result'],
                           prefix='ActionEvents', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='Announcer', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='Assist', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='AssociationName', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='AttendanceRewardsText', retry=NUM_RETRY)

    # skipping AttributeText.json

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='BattleHint', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'summary'], prefix='BattleKeywords', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='BattlePass', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['dlg'], prefix='BattleSpeech', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='BattleUIText', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH,
                           values=['name', 'desc', 'summary', 'variation', 'variation2', 'variation3'],
                           prefix='BuffAbilities', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH,
                           values=['name', 'desc', 'summary'],
                           prefix='Bufs', retry=NUM_RETRY)

    # skipping Characters.json and ChapterBannerConfig.json

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ChoiceEvent', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Coupon', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DailyLoginEvent', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['desc', 'rawDesc'], prefix='DanteAbility.json', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DanteAbilityUIText', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DawnOfGreen', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DungeonArea', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='DungeonName', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='DungeonNode', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['description'], prefix='DungeonStartBuffs', retry=NUM_RETRY)

    # skipping DungeonText.json

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='EGO_Get', retry=NUM_RETRY)

    # skipping EGOgift.json

    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'simpleDesc'], prefix='EGOgift_', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='EgoGiftCategory', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='Egos.json', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='Enemies', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Event', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='FAQ', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='FileDownload', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Filter', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Formation', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='GachaTitle', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='HellsChicken.json', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='HellsChickenDungeon', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='IAPProduct', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='IAPSticker', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='IntegrateAccountUI', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name', 'description'], prefix='IntroduceCharacter', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Introduction', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'flavor'], prefix='Items', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='KeywordDictionary', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='kr_settings', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='LoginUI', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MainUI', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['add', 'min'], prefix='MentalCondition', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonAbName', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonBattle', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonEgo', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonEnemy', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonName', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='MirrorDungeonNode', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='MirrorDungeonTheme', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonUI', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MissionUI', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH,
                           values=['panicName', 'lowMoraleDescription', 'panicDescription'],
                           prefix='PanicInfo', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'summary'], prefix='Passive', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH,
                           values=['title', 'name', 'nameWithTitle', 'desc'],
                           prefix='Personalities',
                           retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Personality', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Quest', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='RailwayDungeon.json', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='RailwayDungeonBuff', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='RailwayDungeonNode', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH,
                           values=['content', 'nameList', 'shortName'],
                           prefix='RailwayDungeonStation',
                           retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='RailwayDungeonUI', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ResistText', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ReturnPolicy', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='RewardDungeon', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='SeasonTitle', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ShopItemCount', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ShotcutKey', retry=NUM_RETRY)

    # ! pm-bots

    utils.translate_prefix(BASE_PATH,
                           values=['levelList', 'abName', 'name', 'desc', 'coinlist', 'coindescs', 'desc'],
                           prefix='Skills', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='SkillTag', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH,
                           values=['company', 'area', 'chapter', 'chaptertitle', 'timeline'],
                           prefix='StageChapter', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['title', 'place', 'desc'], prefix='StageNode', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['parttitle'], prefix='StagePart', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='StoryDungeonUI', retry=NUM_RETRY)

    # skipping StoryText.json (test file)

    # ! FINISHED
    utils.translate_prefix(BASE_PATH, values=['content', 'title', 'desc'], prefix='StoryTheater', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='StoryUIText', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='SuccessRate', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='ThreadDungeon', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Tutorial', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UI_', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UnitKeyword', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['openCondition', 'askLevelUp'], prefix='UnlockCode', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UpgradeCharacter', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UserAgreements', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='UserBanner', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UserInfo', retry=NUM_RETRY)
    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='UserTicket', retry=NUM_RETRY)

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Walpu', retry=NUM_RETRY)

    if 'LimbusLocalize_BIE.dll' in os.listdir(BUILD_PATH):
        shutil.copy('LimbusLocalize_BIE.dll', os.path.join(BUILD_PATH, 'LimbusLocalize_BIE.dll'))
