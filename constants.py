ONE_CHAR = 1
TWO_CHAR = 2

GIVEN_NAME = 'given name'
FAMILY_NAME = 'family name'

FAMILY_NAME_PREFIX_PLESIONYMS = [
    ("mac", "mc", "mck", "mhic", "mic", )
    , ("mellom", "myljom", )
    , ("ned",  "nedre", )
    , ("nic",  "ni", )
    , ("nord",  "norr", )
    , ("ua",  "ui",  "o", )
    , ("opp",  "upp", )
    , ("ost",  "oster", "ostre", )
    , ("ovste", "ovre",  "over", )
    , ("putra", "putera", )
    , ("putri", "puteri", )
    , ("setia", "setya", )
    , ("soder ", "sor ", "sonder", "syd ", "sondre ", "syndre",  "sore", )
    , ("van de", "van den ", "van der", "van het ", "van t", )
    , ("vast", "vaster", )
    , ("verch", "erch", )
    , ("vesle", "vetle", )
    , ("fetch", "vetch", )
    , ("ben", "bin", "ibn", )
    , ("bath", "bar", )
    , ("aust", "austre", )
    , ("dela", "de la", "della", )
    , ("dele", "de le", "delle", )
    , ]

# common variations, diminutives, alternate/foriegn spelling and common mispellings
# lower case, unicode, non ascii characters converted to the base ascii character
FIRST_NAME_PLESIONYMS = [
("shashi", "shashee", "shashiraj", "shashikant", "shashwat", "shashindra", "shashivarnam"
     , "shashanka", "shashishekhar", )
, ("joseph", "joe", "jo", "joey", "jojo", "jolene", "joanne", "jose", "giuseppe", "youssef"
            , "joss", "seph", "josef", 'joanne', "josip", "yusuf", "iosif", "jozsef", )
, ("david", "dave", "davey", "davo", "davy", "davie", "daoud", "dauf", "davide", "davidde"
        , "davito", "dawid", )
, ("josh", "joshua", "joaquim", "joaquin", "joshuah", "joshawa", "joshu", )
, ("richard", "rich", "rick", "ricky", "dick", "dicky", "richy", "ritchie", "ricardo", "rikard"
        , "ryszard", "riccardo", "rikhard", "rikarudo", "rikhardo", "rickard", "ric", )
, ("tom", "thomas", "tommie", "tam", "tomas", "tomasso", "tomaz", "tonis", "toumas", "thoma"
        , "tomohisa", "thom", "tomo", "thomo", "tomi", "tommy", "tomas", "tomasz", "toma", )
, ("william", "willaim", "will", "bill", "willy", "willie", "billie", "billy", "liam", "guillermo"
        , "wilhelm", "vilhelm", "guglielmo", "viljami", "vilmos", "wiliam", "uilleam", "willem", )
, ("elizabeth", "liz", "lizzie", "lizzy", "lizz", "beth", "betsy", "eliza", "libby", "lib", "elisabeth"
        , "elspeth", "elizaveta", "elżbieta", "elisabeta", "elisa", "elise", "eilís", "elikapeka"
        , "lizbet", )
, ("emily", "em", "emmie", "emmy", "emilia", "emilie", "emilija", "emeline", "amalia", "amelie"
        , "emi", "emmi", "emeline", "emil", "emile", )
, ("hannah", "hanne", "hanna", "hannie", "hanny", "hanna", "hann", "han", "hani", "chana", )
, ("jacob", "jake", "jacobus", "jakob", "jakup", "kuba", "yaakov", "yakup", "jakub", "jacopo", "jacques"
        , "giacomo", "jago", "jaakko", "jakup", )
, ("james", "jim", "jimmy", "jami", "jaimie", "jaime", "jaimee", "jamey", "jayme", "jakim"
        , "jacques", "jamie", "jamsie", "seamus", )
, ("jennifer", "jen", "jenn", "jenny", "jenna", "jenni", "jennica", "genevieve", "genevieve", "ginevra", )
, ("john", "jon", "jonny", "jonathon", "jonah", "johan", "joão", "johann", "johannes", "juan"
        , "ivan", "ioan", "eoin", "sean", "shaun", "shawn", "jovica", )
, ("josephine", "josephina", "josie", "josey", "jo", "jojo", "joey", "josette", "josiane", )
, ("julie", "jules", "juliette", "juliet", "juliana", "julianne", "julietta", "julianna", "julinka"
        , "jule", "julka", "yuliana", "yuliyana", "yulia", "yulka", "julia", "julija", "julita", )
, ("katherine", "kate", "kat", "katie", "kathy", "kathie", "katy", "katia", "katrin", "katrine"
        , "katerina", "katarina", "kathryn", "katharine", "katharina", "katalin", )
, ("lisa", "lisette", "lisbeth", "lisbet", "lizbeth", "elisabeth", "elizabeth", "liz", "lizzie", "lizzy",)
,  ("margaret", "maggie", "maggy", "marge", "margie", "meg", "peg", "peggy", "marjorie", "mairead"
        , "margaux", "margot", "margita", "margareta", "margarete", "margarita", "margarid", "margarida", )
, ("mary", "marie", "maria", "marian", "marianne", "maryann", "marilyn", "marlene", "marleen", "marlys"
        , "marylou", "maryjo", "mariza", "mariska", "marisela", "mariska", "maire", )
, ("matthew", "matt", "matty", "mateo", "mathias", "matias", "mads", "matteo", "mattia"
        , "mateusz", "matej", "mattea", "matheo", )
, ("michael", "mike", "mikey", "mickey", "mitch", "micah", "mikhail", "michal", "michelle", "micaela"
        , "michał", "mika", "mykola", "mikkel", )
, ("nicole", "nicki", "nikki", "nikole", "nikoleta", "nikolina", "nichole", "nicolina", "nicollette", )
, ("patrick", "pat", "paddy", "patty", "patrice", "patrizio", "patryk", "patrik", )
, ("peter", "pete", "petey", "pierce", "pieter", "pedro", "petur", "petur", "petra", "petros"
        , "piotr", "pyotr", "petru", "petar", "petri", )
, ("philip", "phil", "phillip", "phill", "philly", "filip", "felipe", "philibert", "philiberto", )
, ("robert", "rob", "robbie", "bobby", "bob", "roberto", "robb", "robby", "bert", "bertie", "robbert"
        , "robertas", "robrecht", "robert", )
, ("samantha", "sam", "sammie", "sammy", "samatha", "samanta", "samira", "samuela", "samuella"
        , "samuela", )
, ("sarah", "sara", "sarai", "sari", "sarra", "sariah", "sari", )
, ("stephanie", "steph", "stephy", "steffie", "stef", "stefanie", "stephanie", "stefano", )
, ("susan", "sue", "susie", "suzy", "suzie", "suzi", "suzanne", "suzanna", "suzannah", "zuzana"
        , "susi", "suse", "suzon", "susana", "susanna", "susi", "suzon", )
, ("timothy", "tim", "timmy", "timothee", "timofey", "timo", "tomasz", "tymoteusz", "timoteo", )
, ("victoria", "vicky", "vicki", "vic", "tori", "torie", "toria", "vittoria", "victoire", "viktoria"
        , "viktorija", "victorina", "vika", "viki", "vica", "victoria", "victorine", "victoriana"
        , "victorine", )
, ("zachary", "zach", "zack", "zac", "zaki", "zak", )
, ("alexander", "alex", "alec", "aleck", "sasha", "xander", "lex", "lexi", "lexie", "lexy", )
, ("daniel", "dan", "danny", "dane", "danielo", "dani", "danilo", )
, ("george", "georgie", "georgina", "georgia", "georgios", "giorgio", "giorgos", "gjorgji", "gorge", )
, ("julius", "jules", "julio", "julien", "juliana", "julie", "julian", "juliet", "juliette", )
, ("lucas", "luke", "luc", "lucky", "luca", "luka", "lucio", "lucian", "lucius", )
, ("megan", "meg", "meggie", "meggy", "meagan", "meaghan", "meganne", "meghan", )
, ("nathan", "nate", "nat", "nathaniel", "nathanael", "nathanial", "nathen", "natanael", "nathaniele", )
, ("oliver", "ollie", "olli", "olivier", "oliva", "oliviero", "olivio", "olivian", )
, ("rachel", "rachael", "raquel", "rachelle", "racquel", "racheal", "rachele", "rachal", )
, ("sophie", "sofie", "sofia", "sofi", "sofía", "sofija", "zsofia", )
, ("vivian", "vivien", "vivienne", "viv", "vivi", "vivia", )

]

""" 
    everything below commented out.  unused but retained for now in case we decide to use title 
    or suffix, we remove nameparser or we take a tack and get fancy
"""

# TITLE_PLESIONYMS  = [
#     ('mr', 'mister', 'mx', 'master', )
#     , ("ms", "mx", "mrs", "miss", "madame", "madam", )
#     , ("dr",  "doctor", )
#     ]

# components of titles that may be followed  or preceeded by other words that are also part of the title
# COMPOUND_TITLE_KEY_WORDS = (
#       "minister", "secretary", "governor", "president", "councillor", "chief", "master", "vice"
#       )

# not being arrogantly english speaking, it is to guess what a lazy person would type on a US keyboard
# in lieu of the correct character (if they meant "ӓ" (a diaeresis) , they'd type "a"
# wanted to call thes dict the ALABAMA_DEPT_OF_REVENUE_TRANSLIT_TABLE... not what they should enter,
# but when a lazy person sees a character not on thieir keyboard, they press the key that looks closest
# TODO: find out why Nor/Danish ø did not come up when generated
# TRANSLITERATION_DICT = {
#     "à": "a", "a": "a", "â": "a", "ã": "a", "ä": "a", "å": "a", "ā": "a", "ă": "a", "ą": "a"
#     , "ǎ": "a", "ǟ": "a", "ǡ": "a", "ǻ": "a", "ȁ": "a", "ȃ": "a", "e": "e", "e": "e", "ê": "e"
#     , "ë": "e", "ē": "e", "ĕ": "e", "ė": "e", "ę": "e", "ě": "e", "𝚎": "e", "ì": "i", "í": "i"
#     , "î": "i", "ï": "i", "ĩ": "i", "ī": "i", "ĭ": "i", "į": "i", "ǐ": "i", "ȉ": "i", "ȋ": "i"
#     , "ḭ": "i", "ḯ": "i", "ỉ": "i", "ị": "i", "ò": "o", "o": "o", "ô": "o", "õ": "o", "ö": "o"
#     , "ō": "o", "ŏ": "o", "ő": "o", "ơ": "o", "ǒ": "o", "ǫ": "o", "ǭ": "o", "ȍ": "o", "ȏ": "o"
#     , "ȫ": "o", "ȭ": "o", "ȯ": "o", "ȱ": "o", "ṍ": "o", "ṏ": "o", "ṑ": "o", "ṓ": "o", "ọ": "o"
#     , "ỏ": "o", "ố": "o", "ồ": "o", "ổ": "o", "ỗ": "o", "ộ": "o", "ớ": "o", "ờ": "o", "ở": "o"
#     , "ỡ": "o", "ợ": "o", "ù": "u", "ú": "u", "û": "u", "ü": "u", "ũ": "u", "ū": "u", "ŭ": "u"
#     , "ů": "u", "ű": "u", "ų": "u", "ư": "u", "ǔ": "u", "ǖ": "u", "ǘ": "u", "ǚ": "u", "ǜ": "u"
#     , "ȕ": "u", "ȗ": "u", "ṳ": "u", "ṵ": "u", "ṷ": "u", "ṹ": "u", "ṻ": "u", "ụ": "u", "ủ": "u"
#     , "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u", "ý": "y", "ÿ": "y", "ŷ": "y", "ȳ": "y"
#     , "ẏ": "y", "ẙ": "y", "ỳ": "y", "ỵ": "y", "ỷ": "y", "ỹ": "y",
#     }
