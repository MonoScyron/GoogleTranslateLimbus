import os
import utils
import shutil

from src.const import BASE_PATH, BUILD_PATH, STORY_PATH, ANNOUNCER_PATH, ID_PATH, EGO_PATH

if __name__ == '__main__':
    utils.translate(STORY_PATH, ['content', 'teller', 'title', 'place'])  # story
    utils.translate(ANNOUNCER_PATH, ['dlg'])  # announcers
    utils.translate(ID_PATH, ['dlg'])  # id dialogue
    utils.translate(EGO_PATH, ['dlg'])  # ego dialogue

    utils.translate_prefix(BASE_PATH, ['teller', 'dialog'], prefix='AbDlg_')

    # todo: value "title" is sus
    abs_event_values = ['title', 'eventDesc', 'prevDesc', 'behaveDesc', 'successDesc', 'failureDesc']
    utils.translate_prefix(BASE_PATH, values=abs_event_values, prefix='AbEvents.json')
    utils.translate_prefix(BASE_PATH, values=abs_event_values, prefix='AbEvents-')
    utils.translate_prefix(BASE_PATH, values=abs_event_values, prefix='AbEvents_')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='AbEventsResultLog')

    utils.translate_prefix(BASE_PATH,
                           values=['name', 'clue', 'storyList', 'story', 'codeName'],
                           prefix='AbnormalityGuides')

    utils.translate_prefix(BASE_PATH,
                           values=['name', 'subDesc', 'desc', 'options', 'message', 'messageDesc', 'result'],
                           prefix='ActionEvents')

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='Announcer')
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='Assist')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='AssociationName')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='AttendanceRewardsText')

    # skipping AttributeText.json

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='BattleHint')
    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'summary'], prefix='BattleKeywords')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='BattlePass')

    utils.translate_prefix(BASE_PATH, values=['dlg'], prefix='BattleSpeech')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='BattleUIText')

    utils.translate_prefix(BASE_PATH,
                           values=['name', 'desc', 'summary', 'variation', 'variation2', 'variation3'],
                           prefix='BuffAbilities')
    utils.translate_prefix(BASE_PATH,
                           values=['name', 'desc', 'summary'],
                           prefix='Bufs')

    # skipping Characters.json and ChapterBannerConfig.json

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ChoiceEvent')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Coupon')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DailyLoginEvent')

    utils.translate_prefix(BASE_PATH, values=['desc', 'rawDesc'], prefix='DanteAbility.json')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DanteAbilityUIText')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DawnOfGreen')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='DungeonArea')

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='DungeonName')
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='DungeonNode')
    utils.translate_prefix(BASE_PATH, values=['description'], prefix='DungeonStartBuffs')

    # skipping DungeonText.json

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='EGO_Get')

    # skipping EGOgift.json

    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'simpleDesc'], prefix='EGOgift_')
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='EgoGiftCategory')

    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='Egos.json')
    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='Enemies')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Event')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='FAQ')

    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='FileDownload')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Filter')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Formation')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='GachaTitle')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='HellsChicken.json')
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='HellsChickenDungeon')

    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='IAPProduct')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='IAPSticker')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='IntegrateAccountUI')

    utils.translate_prefix(BASE_PATH, values=['name', 'description'], prefix='IntroduceCharacter')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Introduction')

    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'flavor'], prefix='Items')

    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='KeywordDictionary')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='kr_settings')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='LoginUI')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MainUI')

    utils.translate_prefix(BASE_PATH, values=['add', 'min'], prefix='MentalCondition')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonAbName')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonBattle')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonEgo')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonEnemy')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonName')
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='MirrorDungeonNode')
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='MirrorDungeonTheme')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MirrorDungeonUI')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='MissionUI')

    utils.translate_prefix(BASE_PATH,
                           values=['panicName', 'lowMoraleDescription', 'panicDescription'],
                           prefix='PanicInfo')

    utils.translate_prefix(BASE_PATH, values=['name', 'desc', 'summary'], prefix='Passive')

    utils.translate_prefix(BASE_PATH, values=['title', 'name', 'nameWithTitle', 'desc'], prefix='Personalities')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Personality')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Quest')

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='RailwayDungeon.json')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='RailwayDungeonBuff')
    utils.translate_prefix(BASE_PATH, values=['title', 'desc'], prefix='RailwayDungeonNode')
    utils.translate_prefix(BASE_PATH, values=['content', 'nameList', 'shortName'], prefix='RailwayDungeonStation')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='RailwayDungeonUI')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ResistText')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ReturnPolicy')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='RewardDungeon')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='SeasonTitle')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ShopItemCount')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='ShotcutKey')

    utils.translate_prefix(BASE_PATH,
                           values=['levelList', 'abName', 'name', 'desc', 'coinlist', 'coindescs', 'desc'],
                           prefix='Skills')
    utils.translate_prefix(BASE_PATH, values=['name'], prefix='SkillTag')

    utils.translate_prefix(BASE_PATH,
                           values=['company', 'area', 'chapter', 'chaptertitle', 'timeline'],
                           prefix='StageChapter')
    utils.translate_prefix(BASE_PATH, values=['title', 'place', 'desc'], prefix='StageNode')
    utils.translate_prefix(BASE_PATH, values=['parttitle'], prefix='StagePart')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='StoryDungeonUI')

    # skipping StoryText.json (test file)

    utils.translate_prefix(BASE_PATH, values=['content', 'title', 'desc'], prefix='StoryTheater')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='StoryUIText')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='SuccessRate')

    utils.translate_prefix(BASE_PATH, values=['name'], prefix='ThreadDungeon')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Tutorial')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UI_')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UnitKeyword')

    utils.translate_prefix(BASE_PATH, values=['openCondition', 'askLevelUp'], prefix='UnlockCode')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UpgradeCharacter')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UserAgreements')
    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='UserBanner')
    utils.translate_prefix(BASE_PATH, values=['content'], prefix='UserInfo')
    utils.translate_prefix(BASE_PATH, values=['name', 'desc'], prefix='UserTicket')

    utils.translate_prefix(BASE_PATH, values=['content'], prefix='Walpu')

    shutil.copy('LimbusLocalize_BIE.dll', os.path.join(BUILD_PATH, 'LimbusLocalize_BIE.dll'))
