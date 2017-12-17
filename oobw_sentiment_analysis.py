import nltk
from nltk.corpus import stopwords
from nltk import tokenize
import nltk.data
import urllib2
import urllib
import json
from pprint import pprint

a = []

aspect_list=["sound","price","quality","bass","volume"]
aspect_dictionary_json_data='{ "sound" : "sound" , "noise" : "sound" , "voice" : "sound" , "audio" : "sound" , "chirp" : "sound" , "murmur" : "sound" , "music" : "sound" , "thud" : "sound" , "thump" : "sound" , "cry" : "sound" , "growl" : "sound" , "peal" : "sound" , "clang" : "sound" , "song" : "sound" , "tone" : "sound" , "roar" : "sound" , "twang" : "sound" , "hiss" : "sound" , "screech" : "sound" , "chorus" : "sound" , "whistle" : "sound" , "sound" : "sound" , "noise" : "sound" , "voice" : "sound" , "music" : "sound" , "audio" : "sound" , "song" : "sound" , "whistle" : "sound" , "bell" : "sound" , "tone" : "sound" , "seem" : "sound" , "thump" : "sound" , "murmur" : "sound" , "cry" : "sound" , "thud" : "sound" , "roar" : "sound" , "drum" : "sound" , "hiss" : "sound" , "ring" : "sound" , "peal" : "sound" , "chime" : "sound" , "sound" : "sound" , "unsound" : "sound" , "sound" : "sound" , "noise" : "sound" , "sensible" : "sound" , "prudent" : "sound" , "chirp" : "sound" , "audio" : "sound" , "defensible" : "sound" , "voice" : "sound" , "wise" : "sound" , "vibration" : "sound" , "rational" : "sound" , "acoustic" : "sound" , "growl" : "sound" , "rumble" : "sound" , "solid" : "sound" , "clang" : "sound" , "scream" : "sound" , "shriek" : "sound" , "ring" : "sound" , "seem" : "sound" , "chime" : "sound" , "look" : "sound" , "whistle" : "sound" , "resound" : "sound" , "reverberate" : "sound" , "rumble" : "sound" , "rattle" : "sound" , "drone" : "sound" , "voice" : "sound" , "purr" : "sound" , "appear" : "sound" , "hum" : "sound" , "beep" : "sound" , "clang" : "sound" , "whir" : "sound" , "resonate" : "sound" , "buzz" : "sound" , "drum" : "sound" , "quality" : "quality" , "character" : "quality" , "tone" : "quality" , "accuracy" : "quality" , "caliber" : "quality" , "credibility" : "quality" , "suitability" : "quality" , "characteristic" : "quality" , "fidelity" : "quality" , "correctness" : "quality" , "ability" : "quality" , "nature" : "quality" , "consistency" : "quality" , "effectiveness" : "quality" , "validity" : "quality" , "appearance" : "quality" , "attribute" : "quality" , "color" : "quality" , "productivity" : "quality" , "adequacy" : "quality" , "excellence" : "quality" , "character" : "quality" , "tone" : "quality" , "excellence" : "quality" , "accuracy" : "quality" , "characteristic" : "quality" , "caliber" : "quality" , "level" : "quality" , "point" : "quality" , "texture" : "quality" , "color" : "quality" , "ability" : "quality" , "clarity" : "quality" , "credibility" : "quality" , "attribute" : "quality" , "nature" : "quality" , "fidelity" : "quality" , "suitability" : "quality" , "appearance" : "quality" , "consistency" : "quality" , "responsiveness" : "quality" , "model" : "quality" , "color" : "quality" , "substandard" : "quality" , "top-notch" : "quality" , "substitute" : "quality" , "quality" : "quality" , "resident" : "quality" , "base" : "quality" , "adult" : "quality" , "editorial" : "quality" , "first-class" : "quality" , "accessibility" : "quality" , "nurse" : "quality" , "hygiene" : "quality" , "firstclass" : "quality" , "shoddy" : "quality" , "material" : "quality" , "driving" : "quality" , "first-rate" : "quality" , "nutritional" : "quality" , "bass" : "bass" , "tuba" : "bass" , "vocalist" : "bass" , "singer" : "bass" , "melody" : "bass" , "guitar" : "bass" , "musician" : "bass" , "trout" : "bass" , "tune" : "bass" , "catfish" : "bass" , "sax" : "bass" , "saxophone" : "bass" , "trombone" : "bass" , "violin" : "bass" , "pike" : "bass" , "drum" : "bass" , "drum" : "bass" , "cello" : "bass" , "percussion" : "bass" , "halibut" : "bass" , "piano" : "bass" , "tuba" : "bass" , "vocalist" : "bass" , "singer" : "bass" , "melody" : "bass" , "tune" : "bass" , "guitar" : "bass" , "musician" : "bass" , "baritone" : "bass" , "pitch" : "bass" , "drum" : "bass" , "sax" : "bass" , "player" : "bass" , "trombone" : "bass" , "piano" : "bass" , "trout" : "bass" , "blues" : "bass" , "saxophone" : "bass" , "vocal" : "bass" , "trumpet" : "bass" , "orchestral" : "bass" , "volume" : "volume" , "book" : "volume" , "bulk" : "volume" , "novel" : "volume" , "hardcover" : "volume" , "journal" : "volume" , "paperback" : "volume" , "capacity" : "volume" , "album" : "volume" , "publication" : "volume" , "magnitude" : "volume" , "notebook" : "volume" , "scrapbook" : "volume" , "swell" : "volume" , "diary" : "volume" , "chamber" : "volume" , "anthology" : "volume" , "copy" : "volume" , "article" : "volume" , "reserve" : "volume" , "tome" : "volume" , "book" : "volume" , "bulk" : "volume" , "paperback" : "volume" , "publication" : "volume" , "journal" : "volume" , "hardcover" : "volume" , "novel" : "volume" , "loudness" : "volume" , "capacity" : "volume" , "album" : "volume" , "crescendo" : "volume" , "voluminous" : "volume" , "loud" : "volume" , "edition" : "volume" , "work" : "volume" , "copy" : "volume" , "diary" : "volume" , "trade" : "volume" , "collection" : "volume" , "swell" : "volume" , "price" : "price" , "cost" : "price" , "price" : "price" , "rate" : "price" , "purchase" : "price" , "purchase" : "price" , "cost" : "price" , "value" : "price" , "market" : "price" , "toll" : "price" , "fare" : "price" , "costly" : "price" , "pricey" : "price" , "purchaser" : "price" , "listprice" : "price" , "overpriced" : "price" , "discount" : "price" , "offer" : "price" , "discount" : "price" , "surcharge" : "price" , "cost" : "price" , "value" : "price" , "rate" : "price" , "toll" : "price" , "listprice" : "price" , "price" : "price" , "fare" : "price" , "charge" : "price" , "exchangerate" : "price" , "market" : "price" , "surcharge" : "price" , "servicecharge" : "price" , "expenditure" : "price" , "inflation" : "price" , "sale" : "price" , "offer" : "price" , "tariff" : "price" , "fee" : "price" , "premium" : "price" , "cost" : "price" , "overpriced" : "price" , "price" : "price" , "discount" : "price" , "inexpensive" : "price" , "rig" : "price" , "affordable" : "price" , "pricey" : "price" , "cheap" : "price" , "expensive" : "price" , "discount" : "price" , "ascertain" : "price" , "determine" : "price" , "set" : "price" , "sold" : "price" , "subsidized" : "price" , "place" : "price" , "rate" : "price" , "package" : "price" , "furnished" : "price" }'
a_dict = json.loads(aspect_dictionary_json_data)
aspect_val_json_data='{"sound" : "0", "price" : "0", "quality" : "0", "bass" : "0", "volume" : "0"}'
aspect_val=json.loads(aspect_val_json_data)
#print a_dict['two'];


text_file = open("C:/Users/shivama/Desktop/OOBW/output.txt", "w+")
text_file.write("\n review_id , asin , review_title , review , rating , confident , segment , sound , price , quality , bass , volume")
for line in open('C:/Users/shivama/Desktop/OOBW/reviews.txt','r').readlines():
    line=line.replace(',','')
    #print line.replace('\t',',')
    line=line.replace('\t',',')
    line=line.replace('<br />','. ')   # replace "<br />" with ". "
    #line=line.replace('"','').replace('/','').replace('\\','').replace('\?','').replace('!','').replace(':','').replace(';','').replace('#','').replace('\(','').replace('\)','')
    columns = line.split(',')
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    #review_data = open("C:/Users/shivama/Desktop/OOBW/reviews.txt").readlines()
    #review_data = " ".join(review_data)
    review_data = columns[3].lower() # convert the text fragment into lower case data and store it in "review_data"
    token_sent = sent_detector.tokenize(review_data.strip())
    for x in token_sent:
        x_split = x.split()
        token_sent_refined = [ i for i in x_split if not i in stopwords.words('english') ]
        token_sent_refined_final = " ".join(token_sent_refined)
        a.append(token_sent_refined_final)
    print a
    print len(a)


    #split_data = review_data.split()
    #split_data = [ x.lower() for x in split_data ]
    #split_data_refined = [ i for i in split_data if not i in stopwords.words('english') ]
    #joined_data = " ".join(split_data_refined)
    #print joined_data



    #print('\n-----\n'.join(sent_detector.tokenize(joined_data.strip())))

    # For using the API to get the sentiment output
    for y in a:
        print y
        # split the text
        y=y.replace('\"','').replace('.','').replace('\/','').replace('\\','').replace('\?','').replace('!','').replace(':','').replace(';','').replace('#','').replace('\(','').replace('\)','')
        words = y.split()
        aspect_val['sound']=0
        aspect_val['price']=0
        aspect_val['quality']=0
        aspect_val['bass']=0
        aspect_val['volume']=0
        # for each word in the line:
        for word in words:

            # prints each word on a line
            print(word)
            check=word in aspect_list
            #print check
            if check:
                aspect_res=a_dict[word]
                print aspect_res
                aspect_val[aspect_res]=aspect_val[aspect_res]+1
                print aspect_val[aspect_res]
        print aspect_val['sound'] , aspect_val['price'] , aspect_val['quality'] , aspect_val['bass'] , aspect_val['volume']
            #print a_dict[word]
        data = urllib.urlencode({"txt":y})
        u = urllib.urlopen("http://sentiment.vivekn.com/api/text/", data)
        the_page = u.read()
        #print the_page
        data = json.loads(the_page)
        print data
        #pprint(data)
        #for key, value in data.items():
        #    print key,value
        #    text_file = open("C:/Downloads/OOB/output.txt", "a")
        #    text_file.write("\n Purchase Amount: %s"%value)
        #    text_file.close()
        #text_file = open("C:/Downloads/OOB/output.txt", "w+")
        probability=json.dumps(data["result"])
        print probability
        probability_json=json.loads(probability)
        print columns[0] , columns[1] , columns[2] , y , columns[4].replace('\n','') , probability_json["confidence"] , probability_json["sentiment"]
        text_file.write("\n%s"%columns[0])
        text_file.write(" , %s"%columns[1])
        text_file.write(" , %s"%columns[2])
        text_file.write(" , %s"%y)
        text_file.write(" , %s"%columns[4].replace('\n',''))
        text_file.write(" , %s"%probability_json["confidence"])
        text_file.write(" , %s"%probability_json["sentiment"])
        text_file.write(" , %s"%aspect_val['sound'])
        text_file.write(" , %s"%aspect_val['price'])
        text_file.write(" , %s"%aspect_val['quality'])
        text_file.write(" , %s"%aspect_val['bass'])
        text_file.write(" , %s"%aspect_val['volume'])
text_file.close()




    #sentences = tokenize.sent_tokentize(joined_data)
    #print sentences
    #for sent in sentences:
    #    print sent
    #joined_data = map(lambda s: s.strip(), joined_data)
    #print joined_data
