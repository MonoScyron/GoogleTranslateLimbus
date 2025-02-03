import os
import utils
import shutil

from const import BASE_PATH, BUILD_PATH, STORY_PATH, ANNOUNCER_PATH, ID_PATH, EGO_PATH, NUM_RETRY

# todo: for all bufs, need to change "name" to original value(?)
#   No!!!! fuck it we bALLLLLLLLLL if shit gets put onto other shit then WHATEVER
#   need to fix one of the bufs that break the skills entirely tho (it's Bufs_Mirror3)
#    - maybe because can't have dup names for bufs?

# todo: Issue with sprite name tags not showing up as sprites, specifically VioletResistDown & Choice_90103301
#   - maybe because can't have dup names for bufs & battle keywords?

LOG = utils.LOG


def copy(filepath: str, override=False):
    path, file = os.path.split(filepath)
    copy_to = os.path.join(BUILD_PATH, path)
    os.makedirs(os.path.dirname(copy_to), exist_ok=True)
    if file in os.listdir(copy_to):
        if not override:
            LOG.info('file {} already exists, skip copying...'.format(file))
            return
        else:
            LOG.info('file {} already exists, overriding'.format(file))
    else:
        LOG.info('copying {}...'.format(file))
    shutil.copy(filepath, os.path.join(BUILD_PATH, filepath))


if __name__ == '__main__':
    utils.translate_regex(STORY_PATH, ['content', 'teller', 'title', 'place'], retry=NUM_RETRY)  # story
    utils.translate(ANNOUNCER_PATH, ['dlg'], retry=NUM_RETRY)  # announcers
    utils.translate(EGO_PATH, ['dlg'], retry=NUM_RETRY)  # ego dialogue
    utils.translate(ID_PATH, ['dlg'], retry=NUM_RETRY)  # id dialogue

    utils.translate_regex('.', ['trans'], p='testing', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, ['teller', 'dialog'], p='AbDlg_', retry=NUM_RETRY)

    # todo: value "title" is sus
    abs_event_values = ['title', 'eventDesc', 'prevDesc', 'behaveDesc', 'successDesc', 'failureDesc']
    utils.translate_regex(BASE_PATH, values=abs_event_values, p='AbEvents.json', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=abs_event_values, p='AbEvents-', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=abs_event_values, p='AbEvents_', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='AbEventsResultLog', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['name', 'clue', 'storyList', 'story', 'codeName'],
                          p='AbnormalityGuides', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['name', 'subDesc', 'desc', 'options', 'message', 'messageDesc', 'result'],
                          p='ActionEvents', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name'], p='Announcer', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name'], p='Assist', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='AssociationName', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='AttendanceRewardsText', retry=NUM_RETRY)

    copy('./EN/AttributeText.json')

    utils.translate_regex(BASE_PATH, values=['content'], p='BattleHint', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name', 'desc', 'summary'], p='BattleKeywords', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='BattlePass', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['dlg'], p='BattleSpeech', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='BattleUIText', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['name', 'desc', 'summary', 'variation', 'variation2', 'variation3'],
                          p='BuffAbilities', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH,
                          values=['name', 'desc', 'summary'],
                          p='Bufs', retry=NUM_RETRY)

    copy('./EN/Characters.json')
    copy('./EN/ChapterBannerConfig.json')

    utils.translate_regex(BASE_PATH, values=['content'], p='ChoiceEvent', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='Coupon', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='DailyLoginEvent', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['desc', 'rawDesc'], p='DanteAbility.json', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='DanteAbilityUIText', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='DawnOfGreen', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='DungeonArea', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name'], p='DungeonName', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['stageList', 'title', 'desc'], p='DungeonNode', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['description'], p='DungeonStartBuffs', retry=NUM_RETRY)

    copy('./EN/DungeonText.json')

    utils.translate_regex(BASE_PATH, values=['content'], p='EGO_Get', retry=NUM_RETRY)

    copy('./EN/EGOgift.json')

    utils.translate_regex(BASE_PATH, values=['name', 'desc', 'simpleDesc'], p='EGOgift_', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name'], p='EgoGiftCategory', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name', 'desc'], p='Egos.json', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name', 'desc'], p='Enemies', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='Event', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='FAQ', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['title', 'desc'], p='FileDownload', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='Filter', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='Formation', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='GachaTitle', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='HellsChicken.json', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['title', 'desc'], p='HellsChickenDungeon', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name', 'desc'], p='IAPProduct', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='IAPSticker', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='IntegrateAccountUI', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name', 'description'], p='IntroduceCharacter', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='Introduction', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name', 'desc', 'flavor'], p='Items', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name', 'desc'], p='KeywordDictionary', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='kr_settings', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='LoginUI', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='MainUI', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['add', 'min'], p='MentalCondition', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='MirrorDungeonAbName', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='MirrorDungeonBattle', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='MirrorDungeonEgo', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='MirrorDungeonEnemy', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='MirrorDungeonName', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['title', 'desc'], p='MirrorDungeonNode', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name'], p='MirrorDungeonTheme', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='MirrorDungeonUI', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='MissionUI', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['panicName', 'lowMoraleDescription', 'panicDescription'],
                          p='PanicInfo', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name', 'desc', 'summary'], p='Passive', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['title', 'name', 'nameWithTitle', 'desc'],
                          p='Personalities',
                          retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='Personality', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='Quest', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name'], p='RailwayDungeon.json', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='RailwayDungeonBuff', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['title', 'desc'], p='RailwayDungeonNode', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH,
                          values=['content', 'nameList', 'shortName'],
                          p='RailwayDungeonStation',
                          retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='RailwayDungeonUI', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='ResistText', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='ReturnPolicy', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='RewardDungeon', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='SeasonTitle', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='ShopUI', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='ShopItemCount', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='ShotcutKey', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['levelList', 'abName', 'name', 'desc', 'coinlist', 'coindescs', 'desc'],
                          p='Skills', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name'], p='SkillTag', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH,
                          values=['company', 'area', 'chapter', 'chaptertitle', 'timeline'],
                          p='StageChapter', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['title', 'place', 'desc'], p='StageNode', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['parttitle'], p='StagePart', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='StoryDungeonUI', retry=NUM_RETRY)

    copy('./EN/StoryText.json')

    utils.translate_regex(BASE_PATH, values=['content', 'title', 'desc'], p='StoryTheater', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='StoryUIText', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='SuccessRate', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['name'], p='ThreadDungeon', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='Tutorial', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='UI_', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='UnitKeyword', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['openCondition', 'askLevelUp'], p='UnlockCode', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='UpgradeCharacter', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='UserAgreements', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name', 'desc'], p='UserBanner', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['content'], p='UserInfo', retry=NUM_RETRY)
    utils.translate_regex(BASE_PATH, values=['name', 'desc'], p='UserTicket', retry=NUM_RETRY)

    utils.translate_regex(BASE_PATH, values=['content'], p='Walpu', retry=NUM_RETRY)
