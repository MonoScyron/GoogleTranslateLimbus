import os
import utils
import shutil

base_path = './EN'
announcer_path = './EN/BattleAnnouncerDlg'
story_path = './EN/StoryData'
id_path = './EN/PersonalityVoiceDlg'
ego_path = './EN/EGOVoiceDig'

utils.translate(story_path, ['content', 'teller', 'title', 'place'])  # story
utils.translate(announcer_path, ['dlg'])  # announcers
utils.translate(id_path, ['dlg'])  # id dialogue
utils.translate(ego_path, ['dlg'])  # ego dialogue

utils.translate_prefix(base_path, ['teller', 'dialog'], prefix='AbDlg_')

# todo: value "title" is sus
abs_event_values = ['title', 'eventDesc', 'prevDesc', 'behaveDesc', 'successDesc', 'failureDesc']
utils.translate_prefix(base_path, values=abs_event_values, prefix='AbEvents.json')
utils.translate_prefix(base_path, values=abs_event_values, prefix='AbEvents-')
utils.translate_prefix(base_path, values=abs_event_values, prefix='AbEvents_')
utils.translate_prefix(base_path, values=['content'], prefix='AbEventsResultLog')

utils.translate_prefix(base_path, values=['name', 'clue', 'storyList', 'story', 'codeName'], prefix='AbnormalityGuides')

utils.translate_prefix(base_path,
                       values=['name', 'subDesc', 'desc', 'options', 'message', 'messageDesc', 'result'],
                       prefix='ActionEvents')

utils.translate_prefix(base_path, values=['name'], prefix='Announcer')
utils.translate_prefix(base_path, values=['name'], prefix='Assist')

utils.translate_prefix(base_path, values=['content'], prefix='AssociationName')
utils.translate_prefix(base_path, values=['content'], prefix='AttendanceRewardsText')

# skipping AttributeText.json

utils.translate_prefix(base_path, values=['content'], prefix='BattleHint')
utils.translate_prefix(base_path, values=['name', 'desc', 'summary'], prefix='BattleKeywords')

utils.translate_prefix(base_path, values=['content'], prefix='BattlePass')

utils.translate_prefix(base_path, values=['dlg'], prefix='BattleSpeech')
utils.translate_prefix(base_path, values=['content'], prefix='BattleUIText')

utils.translate_prefix(base_path,
                       values=['name', 'desc', 'summary', 'variation', 'variation2', 'variation3'],
                       prefix='BuffAbilities')
utils.translate_prefix(base_path,
                       values=['name', 'desc', 'summary'],
                       prefix='Bufs')

# skipping Characters.json and ChapterBannerConfig.json

utils.translate_prefix(base_path, values=['content'], prefix='ChoiceEvent')
utils.translate_prefix(base_path, values=['content'], prefix='Coupon')
utils.translate_prefix(base_path, values=['content'], prefix='DailyLoginEvent')

utils.translate_prefix(base_path, values=['desc', 'rawDesc'], prefix='DanteAbility.json')
utils.translate_prefix(base_path, values=['content'], prefix='DanteAbilityUIText')
utils.translate_prefix(base_path, values=['content'], prefix='DawnOfGreen')
utils.translate_prefix(base_path, values=['content'], prefix='DungeonArea')

utils.translate_prefix(base_path, values=['name'], prefix='DungeonName')
utils.translate_prefix(base_path, values=['title', 'desc'], prefix='DungeonNode')
utils.translate_prefix(base_path, values=['description'], prefix='DungeonStartBuffs')

# skipping DungeonText.json

utils.translate_prefix(base_path, values=['content'], prefix='EGO_Get')

# skipping EGOgift.json

utils.translate_prefix(base_path, values=['name', 'desc', 'simpleDesc'], prefix='EGOgift_')
utils.translate_prefix(base_path, values=['name'], prefix='EgoGiftCategory')

utils.translate_prefix(base_path, values=['name', 'desc'], prefix='Egos.json')
utils.translate_prefix(base_path, values=['name', 'desc'], prefix='Enemies')

utils.translate_prefix(base_path, values=['content'], prefix='Event')
utils.translate_prefix(base_path, values=['content'], prefix='FAQ')

utils.translate_prefix(base_path, values=['title', 'desc'], prefix='FileDownload')

utils.translate_prefix(base_path, values=['content'], prefix='Filter')
utils.translate_prefix(base_path, values=['content'], prefix='Formation')
utils.translate_prefix(base_path, values=['content'], prefix='GachaTitle')

utils.translate_prefix(base_path, values=['content'], prefix='HellsChicken.json')
utils.translate_prefix(base_path, values=['title', 'desc'], prefix='HellsChickenDungeon')

utils.translate_prefix(base_path, values=['name', 'desc'], prefix='IAPProduct')
utils.translate_prefix(base_path, values=['content'], prefix='IAPSticker')

utils.translate_prefix(base_path, values=['content'], prefix='IntegrateAccountUI')

utils.translate_prefix(base_path, values=['name', 'description'], prefix='IntroduceCharacter')
utils.translate_prefix(base_path, values=['content'], prefix='Introduction')

utils.translate_prefix(base_path, values=['name', 'desc', 'flavor'], prefix='Items')

utils.translate_prefix(base_path, values=['name', 'desc'], prefix='KeywordDictionary')

utils.translate_prefix(base_path, values=['content'], prefix='kr_settings')
utils.translate_prefix(base_path, values=['content'], prefix='LoginUI')
utils.translate_prefix(base_path, values=['content'], prefix='MainUI')

utils.translate_prefix(base_path, values=['add', 'min'], prefix='MentalCondition')

utils.translate_prefix(base_path, values=['content'], prefix='MirrorDungeonAbName')
utils.translate_prefix(base_path, values=['content'], prefix='MirrorDungeonBattle')
utils.translate_prefix(base_path, values=['content'], prefix='MirrorDungeonEgo')
utils.translate_prefix(base_path, values=['content'], prefix='MirrorDungeonEnemy')
utils.translate_prefix(base_path, values=['content'], prefix='MirrorDungeonName')
utils.translate_prefix(base_path, values=['title', 'desc'], prefix='MirrorDungeonNode')
utils.translate_prefix(base_path, values=['name'], prefix='MirrorDungeonTheme')
utils.translate_prefix(base_path, values=['content'], prefix='MirrorDungeonUI')

utils.translate_prefix(base_path, values=['content'], prefix='MissionUI')

utils.translate_prefix(base_path, values=['panicName', 'lowMoraleDescription', 'panicDescription'], prefix='PanicInfo')

utils.translate_prefix(base_path, values=['name', 'desc', 'summary'], prefix='Passive')

utils.translate_prefix(base_path, values=['title', 'name', 'nameWithTitle', 'desc'], prefix='Personalities')
utils.translate_prefix(base_path, values=['content'], prefix='Personality')

utils.translate_prefix(base_path, values=['content'], prefix='Quest')

utils.translate_prefix(base_path, values=['name'], prefix='RailwayDungeon.json')
utils.translate_prefix(base_path, values=['content'], prefix='RailwayDungeonBuff')
utils.translate_prefix(base_path, values=['title', 'desc'], prefix='RailwayDungeonNode')
utils.translate_prefix(base_path, values=['content', 'nameList', 'shortName'], prefix='RailwayDungeonStation')
utils.translate_prefix(base_path, values=['content'], prefix='RailwayDungeonUI')

utils.translate_prefix(base_path, values=['content'], prefix='ResistText')
utils.translate_prefix(base_path, values=['content'], prefix='ReturnPolicy')
utils.translate_prefix(base_path, values=['content'], prefix='RewardDungeon')
utils.translate_prefix(base_path, values=['content'], prefix='SeasonTitle')
utils.translate_prefix(base_path, values=['content'], prefix='ShopItemCount')
utils.translate_prefix(base_path, values=['content'], prefix='ShotcutKey')

utils.translate_prefix(base_path,
                       values=['levelList', 'abName', 'name', 'desc', 'coinlist', 'coindescs', 'desc'],
                       prefix='Skills')
utils.translate_prefix(base_path, values=['name'], prefix='SkillTag')

utils.translate_prefix(base_path,
                       values=['company', 'area', 'chapter', 'chaptertitle', 'timeline'],
                       prefix='StageChapter')
utils.translate_prefix(base_path, values=['title', 'place', 'desc'], prefix='StageNode')
utils.translate_prefix(base_path, values=['parttitle'], prefix='StagePart')

utils.translate_prefix(base_path, values=['content'], prefix='StoryDungeonUI')

# skipping StoryText.json (test file)

utils.translate_prefix(base_path, values=['content', 'title', 'desc'], prefix='StoryTheater')
utils.translate_prefix(base_path, values=['content'], prefix='StoryUIText')

utils.translate_prefix(base_path, values=['content'], prefix='SuccessRate')

utils.translate_prefix(base_path, values=['name'], prefix='ThreadDungeon')

utils.translate_prefix(base_path, values=['content'], prefix='Tutorial')
utils.translate_prefix(base_path, values=['content'], prefix='UI_')

utils.translate_prefix(base_path, values=['content'], prefix='UnitKeyword')

utils.translate_prefix(base_path, values=['openCondition', 'askLevelUp'], prefix='UnlockCode')

utils.translate_prefix(base_path, values=['content'], prefix='UpgradeCharacter')

utils.translate_prefix(base_path, values=['content'], prefix='UserAgreements')
utils.translate_prefix(base_path, values=['name', 'desc'], prefix='UserBanner')
utils.translate_prefix(base_path, values=['content'], prefix='UserInfo')
utils.translate_prefix(base_path, values=['name', 'desc'], prefix='UserTicket')

utils.translate_prefix(base_path, values=['content'], prefix='Walpu')

shutil.copy('LimbusLocalize_BIE.dll', os.path.join(utils.BUILD_PATH, 'LimbusLocalize_BIE.dll'))
