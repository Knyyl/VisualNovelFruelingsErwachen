define wen = Character("Wendla", what_slow_cps=45, color="#B89A76")
define mom = Character("Frau Bergmann", what_slow_cps=35, color="#a0712a")
define mel = Character("Melchior", what_slow_cps=45, color="#939AAC")
define mor = Character("Moritz", what_slow_cps=25, color="#7F645D")
define erz = Character(None, what_slow_cps=30)
define erzl = Character(None, what_slow_cps=15)
define thea = Character("Thea", what_slow_cps=45, color="#ff9191")
define martha = Character("Martha", what_slow_cps=45, color="#fcb2fc")
define herr = Character("Vermummter Herr", what_slow_cps=30, color="#a1a1a1")
define sonnenstich = Character("Sonnenstich", color="#c8c8ff", what_slow_cps=30)
define knueppeldick = Character("Knüppeldick", color="#ffc8c8", what_slow_cps=30)
define fliegentod = Character("Fliegentod", color="#ffc8ff", what_slow_cps=30)
define zungenschlag = Character("Zungenschlag", color="#c8ffc8", what_slow_cps=30)
define hungergurt = Character("Hungergurt", color="#ffcccc", what_slow_cps=30)
init:
    transform left:
        xalign 0.1
        yalign 1.0
        zoom 0.8

    transform right:
        xalign 0.9
        yalign 1.0
        zoom 0.8

    transform center:
        xalign 0.5
        yalign 1.0
        zoom 0.8

label ende:

    scene black
    with fade
    $ gutene = False
    if moritz_suicide == True and brief_verfassen == True and wendla_aufklaerung != "biologisch" and mel_leben == True and wendla_fragt == True:
        scene schule with fade
        play music "suspence.mp3" fadein 2.0
        erz "Lorekeeper Ende (1/5)"
        erz "Du hast deinen Weg gefunden, zwischen den Zeilen des Schicksals zu wandeln."
        erz "Alles geschah wie im Original – nicht mehr, nicht weniger."
        erz "Es ist weder triumphal noch gänzlich tragisch."
        erz "Du hast die Geschichte bewahrt, so wie sie war, und das ist auch eine Art von Erfolg."

    elif moritz_suicide == True and wendla_aufklaerung != "biologisch" and mel_leben == False:
        play music "bad_ending.mp3" fadein 2.0
        erz "Schlechtes Ende (3/5)"
        erz "Du hast alle in den Abgrund gestoßen."
        erzl "Wendla ist tot."
        erzl "Moritz ist tot."
        erzl "Melchior ist tot."
        erz "Alles, was bleibt, ist ein leerer Friedhof und die Erinnerung an dein Scheitern."
        erz "Ihre Leben hätten gerettet werden können, doch deine Entscheidungen haben sie ins Verderben geführt."
        erz "Du bist schuld an dieser Tragödie. Allein du."

    elif moritz_suicide == False and wendla_aufklaerung == "biologisch" and mel_leben == True and wendla_fragt == False:
        $ gutene = True
        scene wohnzimmer with fade
        play music "emotional_happy.mp3" fadein 2.0
        erz "Gutes Ende (2/5)"
        erz "Herzlichen Glückwunsch!"
        erz "Niemand musste sterben, niemand wurde vergessen."
        erz "Du hast Wendla, Moritz und Melchior vor ihren Abgründen bewahrt und ihnen eine Zukunft gegeben."
        erz "Dies ist der seltene Moment, in dem alles gut ausgeht – und es liegt allein an dir."

    elif moritz_suicide == False and wendla_aufklaerung == "biologisch" and mel_leben == True and wendla_fragt == True:
        scene wohnzimmer with fade
        play music "emotional_happy.mp3" fadein 2.0
        erz "Fast gutes Ende (5/5)"
        erz "Niemand musste sterben, doch Wendla hat einen bleibenden mentalen Schaden."
        erz "Du hast Moritz und Melchior vor ihren Abgründen bewahrt und ihnen eine Zukunft gegeben."

    else:
        scene wald with fade
        play music "suspence.mp3" fadein 2.0
        erz "Neutrales Ende (4/5)"
        erz "Nicht alle haben es geschafft, nicht alle konnten gerettet werden."
        erz "Deine Entscheidungen haben manches Licht am Leben gehalten, aber andere sind in der Dunkelheit erloschen."
        erz "Es ist ein Ende voller Widersprüche – ein Sieg und ein Verlust zugleich."
        erz "Was hätte anders sein können?"

    if gutene == True:
        if moritz_suicide == True:
            show mor_crossed at right
        else:
            show mor_smile at right
        if wendla_aufklaerung != "biologisch":
            show wen_crossed at center
        else:
            show wen_happy at center
        if mel_leben == False:
            show mel_crossed at left
        else:
            show mel_laugh at left
    else:
        if moritz_suicide == True:
            show mor_crossed at right
        else:
            show mor at right
        if wendla_aufklaerung != "biologisch":
            show wen_crossed at center
        else:
            show wen at center
        if mel_leben == False:
            show mel_crossed at left
        else:
            show mel at left

    
    herr "Bist du dir sicher, dass alles so passieren sollte?"
    return


label start:
    jump wendlas_geburtstag_wohnzimmer

label wendla_mutter_wohnzimmer:

    scene wohnzimmer
    with fade

    play music "happy.mp3" fadein 2.0

    show mom_happy at left
    show wen at right

    erz "Die Nachmittagssonne fällt durch das Fenster. Aus dem Flur sind Schritte zu hören, und dann öffnet sich eine Tür."

    mom "Wendla! Wendla, wo bist du?"

    hide wen
    show wen_unhappy at right
    wen "Ich bin hier, Mutter. Was ist los?"

    mom "Ina hat einen Sohn bekommen! Du bist wieder Tante geworden!"

    hide wen_unhappy
    show wen_happy at right
    wen "Einen Sohn? Das ist eine wunderbare Nachricht! Wie geht es ihr?"

    mom "Es geht ihr sehr gut. Ein prächtiger Junge. Hier, nimm diesen Korb für sie, bevor du sie besuchst."

    hide wen_happy
    show wen at right
    wen "Mutter, ich wollte dich etwas fragen... Wie kommen eigentlich Kinder auf die Welt?"

    stop music fadeout 1.0
    play music "dissonant.mp3" fadein 2.0
    hide mom_happy
    show mom_unhappy at left
    mom "Wendla… so etwas fragt man nicht. Das ist nichts für dich."

    hide wen
    show wen_unhappy at right
    wen "Aber ich bin doch kein kleines Kind mehr. Bitte, Mutter. Ich muss es wissen."

    erz "Eine spürbare Spannung liegt in der Luft, als hätte die Frage eine Grenze überschritten."
    erz "Welche Erklärung soll die Mutter geben?"

    menu:
        "Die biologische Erklärung":
            $ wendla_aufklaerung = "biologisch"
            mom "Nun gut… Ein Mann und eine Frau kommen sich sehr nah. Aus dieser Verbindung wächst neues Leben. Es ist nichts Schlimmes, nur schwer in Worte zu fassen."
            wen "Es klingt seltsam, aber vielleicht ist es einfacher, als ich dachte. Danke, Mutter."
            erz "Wendla nickt langsam, ein neues, noch unklar definiertes Verständnis formt sich in ihrem Inneren."

        "Die 'moralische' Erklärung":
            $ wendla_aufklaerung = "moralisch"
            mom "Um ein Kind zu bekommen, muss man seinen Ehemann von ganzem Herzen lieben. Das ist das Wichtigste… mehr musst du nicht wissen."
            wen "Also… das ist alles?"
            mom "Ja, mein Kind. Jetzt geh bitte zu Ina."
            erz "Wendla bleibt für einen Moment reglos stehen, nicht zufrieden mit der Antwort. Doch ihre Mutter wendet den Blick ab, und Wendla erkennt, dass jede weitere Frage sinnlos ist."
    erz "Wendla nimmt den Korb. Die Entscheidung ihrer Mutter hinterlässt einen Eindruck, dessen Bedeutung erst später klar werden wird."

    jump der_heuboden

label der_heuboden:

    scene heu
    with fade

    play music "dissonant.mp3" fadein 2.0

    show mel_unhappy at left
    show wen_unhappy at right

    erz "Wendla klettert die Leiter zum Heuboden hinauf. Die Luft ist schwer, der Duft von Heu und nahendem Regen liegt in der Scheune."

    wen "Melchior? Hier bist du. Alle suchen dich unten, es zieht ein Gewitter auf."

    hide mel_unhappy
    show mel_sus at left
    mel "Geh weg, Wendla. Geh einfach weg."

    wen "Was ist los mit dir? Warum versteckst du dich hier?"

    hide mel_sus
    show mel_unhappy at left
    mel "Ich will allein sein. Du solltest nicht hier sein."

    erz "Das Donnern in der Ferne wird lauter, die Spannung im Heuboden steigt."

    wen "Es ist stickig hier drin. Komm mit raus. Wir könnten noch auf die Matte gehen, bevor der Regen kommt."

    hide mel_unhappy
    show mel_bigworry at left
    mel "Wendla… warum bist du hier?"

    if wendla_aufklaerung == "biologisch":
        wen "Melchior… ich gehe jetzt."

        mel "Nein, bleib… ich…"
        stop music fadeout 2.0
        wen "Lass mich gehen."

        erz "Wendla weicht seinen Händen aus, rutscht zur Leiter zurück und klettert hinunter. Unten bleibt sie kurz stehen, das Herz rast. Dann verschwindet sie schnellen Schrittes."
        stop music fadeout 2.0
    else:
        wen "Melchior… was ist mit dir?"

        erz "Wendla zögert, bleibt sitzen. Sie ahnt nicht, was gleich geschehen wird. Das Donnern rückt näher, die Luft wird drückend."

        scene black with fade
        stop music fadeout 2.0
        menu:
            "Melchior greift Wendla":
                scene black
            "Melchior greift Wendla":
                scene black
            "Melchior greift Wendla":
                scene black

        erz "In der Enge des Heubodens gibt es keinen Widerstand mehr. Was bleibt, ist nur die Stille danach."
    jump moritz_letter_scene
        
label friedhof_szenen:


    scene kirche
    with fade

    show mel at left

    if brief_verfassen:
        play music "suspence.mp3" fadein 2.0
        erz "Melchior stolpert aus der Dunkelheit der Wälder auf den stillen Kirchhof. Sein Atem ist schwer, seine Kleider zerrissen, Schweiß und Schmutz bedecken sein Gesicht."

        mel "Endlich … raus. Aber was jetzt? Was hält mich überhaupt noch?"

        erz "Die Nacht ist kalt, die Luft schwer von Verzweiflung. Melchior erstickt förmlich an Erinnerungen und Schuld."

    else:
        stop music fadeout 1.0
        play music "melchior.mp3" fadein 2.0

        erz "Melchior wandert ziellos durch die dunkle Nacht. Kein Stern durchbricht die Wolkendecke, nur der Mond wirft ein schwaches Licht auf den Weg."

        mel "Alles ist anders … leer. Aber vielleicht gibt es noch einen Weg."
        
        erz "Seine Schritte hallen auf dem Pflaster, während Blätter im Wind rascheln."

    if wendla_aufklaerung != "biologisch":

        erz "Melchior bleibt vor einem Grab stehen. Immergrün umrahmt einen schlichten Stein, auf dem 'Wendla, Selig sind, die reinen Herzens sind...' steht."

        mel "Ich bin dein Mörder. Wie konnte ich dich so im Stich lassen?"

        erz "Der Wind pfeift, und Melchior sinkt auf die Knie."

    if moritz_suicide == True:
        stop music fadeout 1.0
        play music "very_dark.mp3" fadein 2.0

        erz "Eine kühle Brise weht über den Kirchhof, als eine Gestalt vor Melchior auftaucht: Moritz, oder was von ihm blieb, mit dem Kopf unter dem Arm."

        mor "Einen Augenblick, Melchior. Die Gelegenheit wiederholt sich nicht so bald."

        erz "Bevor Melchior reagieren kann, erscheint eine zweite Gestalt – der Vermummte Herr."

        herr "Du stehst an der Schwelle, Junge. Entscheide dich: Willst du weiterleben oder endlich Ruhe finden?"

        erz "Eine Entscheidung steht an."
        menu:
            "Melchior greift nach Moritz’ Hand.":
                $ mel_leben = False
            "Melchior greift nach der Hand des Herrens.":
                $ mel_leben = True

    elif wendla_aufklaerung != "biologisch":
        stop music fadeout 1.0
        play music "very_dark.mp3" fadein 2.0

        mel "Ich verdiene es nicht zu leben. Ich bin ein Mörder."

        erz "Eine Entscheidung steht an."
        menu:
            "Melchior beendet alles und folgt Wendla in den Tod.":
                $ mel_leben = False
            "Melchior rappelt sich auf und beschließt, für Moritz und sich weiterzuleben.":
                $ mel_leben = True

    elif wendla_aufklaerung == "biologisch" and moritz_suicide == False:
        stop music fadeout 1.0
        play music "happy.mp3" fadein 2.0

        erz "Melchior verlässt den Kirchhof und tritt zurück auf den stillen Weg. Trotz der Dunkelheit spürt er eine innere Wärme."

        mel "Wir atmen, wir existieren. Und doch fühlt es sich an, als wären wir längst begraben. Vielleicht ist das Leben einfach so: ein ewiges Umherirren im Dunkeln."

        mel "Aber was soll's? Man geht weiter, weil es nichts anderes gibt. Vielleicht, weil man zu feige ist, stehenzubleiben."
        $ mel_leben = True
    jump ende


label moritz_letter_scene:

    scene brief
    with fade

    play music "melchior.mp3" fadein 2.0

    erz "Ein Brief von Moritz Stiefel erreicht Frau Gabor. Die unsichere Schrift spiegelt seine Verzweiflung wider."
    erz "Er bittet sie flehend um finanzielle Hilfe für eine Flucht nach Amerika, da der Druck der Schule und seiner Eltern ihn zu ersticken droht."
    erz "Zwischen den Zeilen deutet Moritz an, dass er keinen anderen Ausweg sieht."
    erz "Seine Worte sind voller Schmerz, aber auch von der leisen Hoffnung getragen, dass sie ihm helfen wird."

    menu:
        "Frau Gabor besucht Moritz persönlich":
            $ gabor_visits = True
            erz "Nach langem Überlegen beschließt Frau Gabor, Moritz aufzusuchen. Sie kann den Schmerz in seinen Worten nicht ignorieren."
            erz "Trotz ihrer Zweifel macht sie sich auf den Weg, bereit, ihm Trost und Unterstützung zu spenden – wenn auch keine finanzielle Hilfe."

            scene black with fade
            pause 1.0

            if melchior_supports_moritz and gabor_visits:
                $ moritz_suicide = False
            else:
                $ moritz_suicide = True

            jump moritz_monolog_ilse

        "Frau Gabor schreibt einen Brief mit einer Ablehnung":
            $ gabor_visits = False
            erz "Frau Gabor setzt sich an ihren Schreibtisch und schreibt Moritz eine höfliche, aber klare Antwort."
            erz "Sie erklärt, dass sie ihm das Geld für die Überfahrt nicht geben kann und rät ihm, sich seinen Eltern anzuvertrauen."
            erz "Mit schwerem Herzen endet sie den Brief mit allgemeinen Worten des Trostes, doch zwischen den Zeilen bleibt eine spürbare Distanz."

            if melchior_supports_moritz and gabor_visits:
                $ moritz_suicide = False
            else:
                $ moritz_suicide = True

            jump moritz_monolog_ilse
label moritz_monolog_ilse:


    scene nachtfeld
    with fade

    play music "very_dark.mp3" fadein 2.0

    show mor at center

    erz "Moritz steht allein unter dem dunklen Himmel. Er hebt den Blick und scheint etwas Unaussprechliches zu suchen."

    mor "Ich passe nicht hinein, nicht in diese Welt, nicht zu diesen Menschen. Alles, was ich tue, scheint falsch. Sie sagen, ich soll kämpfen, mich bemühen – aber wofür? Für ein Leben, das mich nur zerquetscht?"

    erz "Er schaut zum Himmel, der ruhig wirkt, als sei nie etwas geschehen. In ihm tobt jedoch ein Sturm. Melchior hat es gut gemeint, aber er versteht nicht. Niemand versteht es."

    mor "Es ist, als hätte ich keinen Platz. Man hat mich in diese Welt gedrängt, ohne zu fragen. Jetzt will ich einfach nur weg."

    erz "Plötzlich raschelt es im Gebüsch. Ilse tritt hervor, farbenfroh gekleidet, mit einem seltsamen Ausdruck von Heiterkeit."

    mor "Ilse? Was machst du hier ganz allein?"

    erz "Ilse lächelt geheimnisvoll und nähert sich ein Stück."

    if moritz_suicide == False:

        stop music fadeout 1.0
        play music "emotional_happy.mp3" fadein 2.0
        hide mor
        show mor_smile at center
        erz "Ilse spricht von anderen Orten, anderen Möglichkeiten. Ihre Stimme klingt wie ein ferner Ruf, der Moritz aus seinem Gedankensumpf locken will."

        mor "Vielleicht hast du recht. Vielleicht lohnt es sich doch, weiterzugehen."

        erz "Ilse streckt die Hand aus, lädt ihn ein mitzukommen. Moritz zögert, doch dann nickt er. Gemeinsam verschwinden sie in der Nacht, fort von dem Schatten, der ihn bisher umfangen hielt."

        stop music fadeout 2.0
        jump schwangerschaft

    else:
        stop music fadeout 1.0

        erz "Ilse redet, lacht leise, doch Moritz hört ihre Worte nicht mehr. Er spürt keine Wärme, keine Hoffnung. Ihr Lachen verhallt, und Ilse verschwindet, ohne dass er ihr folgt."
        hide mor
        show mor_suicide at center
        mor "Es hätte nur ein Wort gebraucht…"
        scene black with fade

        menu:
            "Ziel auf deinen Kopf":
                scene black with fade
            "Ziel auf deinen Kopf":
                scene black with fade
            "Ziel auf deinen Kopf":
                scene black with fade
        menu:
            "Drück ab.":
                scene black
            "Drück ab.":
                scene black
            "Drück ab.":
                scene black
        erz "Die Dunkelheit scheint dichter zu werden. Ein entfernter Laut, dann Stille."
        play sound "shoot.mp3"

        scene black with fade

        erz "Die Nacht bleibt stumm, als wäre nie etwas geschehen."

        stop music fadeout 2.0
        jump lehrer_eltern_szenen


label wendla_melchior_wald:

    scene wald
    with fade

    play music "melchior.mp3" fadein 2.0

    if wendla_fragt:

        show wen at right
        show mel_unhappy at left

        erz "Die Sonne scheint durch die Äste, während Wendla und Melchior sich im Wald begegnen."
        mel "Wendla? Was machst du hier ganz allein?"
        wen "Ich habe Waldmeister gesammelt. Aber ich glaube, ich habe mich verlaufen."

        hide mel_unhappy
        show mel at left
        mel "Dann lass uns ein Stück zusammen gehen. Ich zeige dir den Weg zurück."

        erz "Beide gehen eine Weile schweigend. Nach einiger Zeit erreichen sie eine sonnige Lichtung."

        wen "Melchior... ich habe noch nie gespürt, wie es ist, geschlagen zu werden."

        mel "Wendla, warum denkst du über so etwas nach?"

        wen "Martha wird ständig geschlagen... Ich kann es mir nicht vorstellen. Ich will wissen, wie es sich anfühlt."

        hide mel
        show mel_unhappy at left
        mel "Wendla, das ist Unsinn! Niemand sollte so etwas erleben wollen!"

        wen "Bitte, Melchior… schlag mich. Nur einmal."

        erz "Melchior blickt sie fassungslos an."

        mel "Wenn du unbedingt darauf bestehst…"
        
        wen "Ich spüre kaum etwas. Schlag mich fester, Melchior."

        mel "Wendla, hör auf! Was verlangst du da von mir?"
        stop music fadeout 2.0
        erz "Getrieben von einer Mischung aus Wut und Verzweiflung wirft Melchior die Gerte weg und schlägt mit den Fäusten auf Wendla ein."

        scene black with fade
        play sound "punches.mp3"

        wen "Ah! ..."

        erz "Plötzlich lässt Melchior von ihr ab. Tränen laufen über sein Gesicht, während er die Hände an seine Schläfen presst. Ohne ein weiteres Wort stürzt er in den Wald davon, lässt Wendla allein zurück."
        
        stop music fadeout 2.0
        jump wendla_mutter_wohnzimmer

    else:
        
        show wen at right
        show mel at left
        erz "Die Sonne scheint durch die Äste, während Wendla und Melchior sich im Wald begegnen."
        
        mel "Wendla? Was machst du hier allein im Wald?"
        wen "Ich habe Waldmeister gesammelt, aber jetzt habe ich mich verlaufen."

        mel "Komm, ich zeige dir den Weg zurück."

        erz "Sie gehen schweigend durch den Wald."

        hide mel
        show mel_unhappy at left
        mel "Du bist so still. Woran denkst du?"

        hide wen
        show wen_unhappy at right
        wen "An Martha. Sie hat es so schwer. Ich wünschte, ich könnte ihr helfen."

        mel "Manchmal reicht es, einfach da zu sein. Niemand sollte so leiden müssen."

        wen "Ja, das stimmt… Danke, Melchior."

        erz "Beide setzen ihren Weg fort, Wendla mit ihrem Korb, Melchior neben ihr. Das Rauschen der Blätter wird lauter, während sie den Wald verlassen."

        stop music fadeout 2.0
        jump wendla_mutter_wohnzimmer


label melchior_moritz_zimmer:

    scene zimmermel
    with fade

    play music "melchior.mp3" fadein 2.0

    show mel_unhappy at left
    show mor_sad at right

    erz "Der Abend hat sich über Melchiors Zimmer gesenkt. Die Lampe auf dem Schreibtisch flackert leicht, während Moritz und Melchior auf dem Kanapee sitzen und reden."

    mor "Weißt du, Melchior, manchmal frage ich mich… warum wir das alles überhaupt machen. Die Schule, die Prüfungen… wofür?"

    hide mel_unhappy
    show mel at left
    mel "Damit wir werden wie unsere Eltern. Funktionieren, ohne nachzufragen. Aber du bist nicht dafür gemacht, Moritz."

    mor "Manchmal fühle ich mich, als würde ich ertrinken. Jeder Tag ist ein Kampf, und am Ende fragt keiner, ob ich überhaupt noch kann."

    hide mel
    show mel_unhappy at left
    mel "Und du redest mit niemandem darüber?"

    mor "Mit wem denn? Mein Vater würde nur brüllen, dass ich mich zusammenreißen soll. Meine Mutter würde weinen. Was bringt das?"

    stop music fadeout 1.0
    play music "dissonant.mp3" fadein 2.0

    erz "Die Stimmung wird düster, Spannung baut sich auf."


    menu:
        "Melchior unterstützt Moritz emotional und bietet Hilfe an":
            $ melchior_supports_moritz = True

            hide mel_unhappy
            show mel_happy_alt at left
            mel "Hör zu, Moritz. Ich helfe dir. Wir können zusammen lernen, Schritt für Schritt. Und vergiss nicht, dass deine Noten nicht bestimmen, wer du als Mensch bist."

            hide mor_sad
            show mor_smile at right
            mor "Würdest du das wirklich tun? Mit mir lernen?"

            mel "Natürlich. Ich will, dass du dich besser fühlst. Du bist mein Freund, Moritz."

            erz "Die Worte scheinen Moritz zu erreichen. Seine Schultern entspannen sich, und ein schwaches Lächeln huscht über sein Gesicht."

            mor "Danke, Melchior. Das bedeutet mir viel… Ich glaube, ich habe das gebraucht."

            stop music fadeout 1.0
            play music "emotional_happy.mp3" fadein 2.0

            erz "Die Stimmung hält auf, Hoffnung schimmert durch."

            jump wendla_melchior_wald

        "Melchior wechselt das Thema":
            $ melchior_supports_moritz = False

            hide mel_unhappy
            show mel_sus at left
            mel "Es bringt nichts, sich den Kopf über die Schule zu zerbrechen. Lass uns über etwas anderes reden."

            mor "(verwirrt) Etwas anderes? Aber…"

            hide mel_sus
            show mel at left
            mel "Hast du Faust schon zu Ende gelesen? Du wolltest doch wissen, wie die Walpurgisnacht beschrieben wird."

            erz "Moritz nickt langsam, doch sein Blick bleibt schwer. Die Worte, die er sagen wollte, bleiben unausgesprochen, die Last auf seinen Schultern unverändert."

            stop music fadeout 1.0
            play music "story.mp3" fadein 2.0

            jump wendla_melchior_wald


label wendla_thea_martha_wald:

    scene wald
    with fade

    play music "happy.mp3" fadein 2.0

    erz "Die drei Mädchen – Wendla, Thea und Martha – stehen in einer kleinen Lichtung im Wald. Das Zwitschern der Vögel und das Rascheln der Blätter im Wind bilden eine sanfte Kulisse."

    play music "suspence.mp3" fadein 2.0
    martha "Papa schlägt mich krumm, wenn ich was falsch mache, und Mama sperrt mich ins Kohlenloch."
    
    thea "Das ist ja schrecklich, Martha! Wie hältst du das aus?"
    martha "Es ist, wie es ist."

    erz "Wendla steht daneben und lauscht, innerlich bewegt von Marthas Aussage. Eine Frage drängt sich in ihren Kopf."

    menu:
        "Wendla fragt":
            $ wendla_fragt = True
            wen "Womit schlagen sie dich, Martha? Wie fühlt sich das an?"
            martha "Hör auf, Wendla. Das willst du nicht wissen."

            erz "Martha dreht sich weg, ihre Stimme erstickt in der Stille des Waldes. Wendla bleibt stehen, eine seltsame Spannung in ihrem Inneren."
            stop music fadeout 1.0
            play music "very_dark.mp3" fadein 2.0
            scene black
            erz "Marthas Ausweichen löst in ihr nicht nur Verwunderung aus, sondern auch einen unerklärlichen Drang, es selbst zu spüren."

            
            wen "Wie kann man etwas verstehen, wenn man es nie erlebt hat?"
            erz "Die Worte schwingen in Wendlas Kopf nach. Es ist, als hätte sich eine unbekannte Tür in ihr geöffnet, ein Verlangen nach dem Unbekannten, das sie weder benennen noch begreifen kann."

        "Wendla schweigt":
            $ wendla_fragt = False
            erz "Wendla spürt, wie ihr die Frage auf der Zunge brennt, doch sie wagt es nicht, sie auszusprechen."
            erz "Stattdessen beobachtet sie schweigend Marthas Haltung, den gesenkten Blick, den schwachen Windhauch im Haar. Die Spannung bleibt jedoch im Raum."

            stop music fadeout 1.0
            play music "dissonant.mp3" fadein 2.0
            scene black

            wen "(leise zu sich selbst) Vielleicht… vielleicht ist es besser, es nicht zu wissen."

            erz "Die Ungewissheit nagt an Wendla, doch sie beschließt, nicht weiter nachzuhaken. Trotzdem bleibt das Unausgesprochene zwischen ihnen wie ein Schatten im Wald."

    scene wald
    erz "Die drei Mädchen bewegen sich weiter durch den Wald. Die Entscheidung, die Wendla hier getroffen hat, wird später ihre Sicht auf die Welt verändern."

    stop music fadeout 2.0
    jump melchior_moritz_zimmer


label moritz_melchior_schule:

    scene schule
    with fade

    play music "melchior.mp3" fadein 2.0

    show mel_unhappy at left
    show mor_sad at right

    erz "Die anderen Jungen sind längst auf dem Weg nach Hause, doch Moritz und Melchior bleiben zurück. Der Weg ist verlassen, die Luft schwer von der nahenden Nacht."

    mel "Ich bin es so leid. Alles dreht sich nur um diese verdammten Schulaufgaben. Wir werden daran ersticken."

    mor "Sie pressen uns in ein Korsett, Melchior. Nicht nur in der Schule – überall."

    hide mel_unhappy
    show mel_sus at left
    mel "Damit wir genau wie sie werden. Stumpf. Angepasst. Voller Angst vor allem, was anders ist."

    mor "Denkst du, das wird bei uns genauso?"

    hide mel_sus
    show mel at left
    mel "Nur, wenn wir es zulassen. Aber sag mal, Moritz… warum bedrückt dich das alles in letzter Zeit so sehr?"

    hide mor_sad
    show mor_fakesmile at right
    mor "Seit Weihnachten fühle ich mich… seltsam. Alles scheint sich zu verändern, aber ich verstehe nichts davon. Es macht mir Angst."

    stop music fadeout 1.0
    play music "dissonant.mp3" fadein 2.0

    hide mel
    show mel_unhappy at left
    mel "Und du weißt wirklich nicht, warum?"

    hide mor_fakesmile
    show mor_sad at right
    mor "Nein… ich meine, ich ahne etwas. Aber niemand redet darüber. Niemand erklärt uns irgendetwas."

    hide mel_unhappy
    show mel_sus at left
    mel "Es ist doch absurd, nicht? Die Erwachsenen erwarten, dass wir die Welt verstehen, aber sie verweigern uns jede Erklärung."

    mor "Melchior, du weißt doch Dinge. Mehr als ich. Kannst du es mir… erklären?"

    hide mel_sus
    show mel at left
    mel "Was genau möchtest du wissen?"

    mor "Alles. Warum wir diese Gefühle haben. Warum es plötzlich so kompliziert wird, mit den Mädchen zu reden. Was das alles bedeutet."

    erz "Ein sanfter Wind pfeift auf."

    hide mel
    show mel_bigworry at left
    mel "Das ist viel auf einmal, Moritz. Vielleicht… sollten wir ein anderes Mal ausführlicher sprechen."

    mor "Nein, nicht sprechen. Schreib es mir auf. In einem Brief. Alles, was du weißt. Ich kann das nicht hier und jetzt hören."

    hide mel_bigworry
    show mel_sus at left
    mel "Einen Brief? Warum?"

    hide mor_sad
    show mor_fakesmile at right
    mor "Weil ich es besser begreifen kann, wenn ich es allein lese. Und… ich schäme mich zu sehr, es laut zu hören."

    erz "Die Stimmung wird düsterer, fast drängend."

    hide mel_sus
    show mel at left
    mel "Hm. Vielleicht hast du recht. Es könnte einfacher sein, es aufzuschreiben. Aber bist du sicher? Manche Dinge sind schwer zu verdauen."

    hide mor_fakesmile
    show mor_sad at right
    mor "Ich muss es wissen, Melchior. Bitte."

    erz "Ein Entscheidungspunkt nähert sich. Soll Melchior den Brief verfassen oder es lassen?"

    menu:
        "Brief verfassen":
            $ brief_verfassen = True
            hide mel
            show mel at left
            mel "Gut, Moritz. Ich schreibe dir alles auf. So klar und einfach wie möglich."

            hide mor_sad
            show mor_fakesmile at right
            mor "Danke, Melchior. Ich vertraue dir."

            erz "Melchior nickt und blickt nachdenklich in die Ferne. Er ahnt nicht, welche Konsequenzen dieser Brief eines Tages haben könnte."

            stop music fadeout 2.0
            jump wendla_thea_martha_wald

        "Keinen Brief verfassen":
            $ brief_verfassen = False
            stop music fadeout 1.0
            play music "suspence.mp3" fadein 2.0

            erz "Moritz blickt Melchior flehend an. Die Bitte nach einem Brief hängt schwer in der kühlen Abendluft."
            
            hide mel
            show mel_unhappy at left
            mel "Einen Brief?"

            erz "Melchior schweigt, sein Blick gleitet zum Boden. Der Gedanke an Papier und Worte, die für immer festgehalten werden, lässt ihn stocken."

            mel "Nein, Moritz. Das ist zu gefährlich. Was, wenn jemand den Brief findet?"

            erz "Moritz starrt ihn überrascht an, doch Melchior weicht seinem Blick nicht aus."
            mel "Manche Dinge gehören nicht aufs Papier. Nicht so."

            erz "Moritz senkt den Kopf. Man erkennt die Leere in seinen Augen."

            stop music fadeout 2.0
            jump wendla_thea_martha_wald

label lehrer_eltern_szenen:
    if not moritz_suicide:
        jump schwangerschaft


    if brief_verfassen == False:

        scene schule
        with fade

        play music "very_dark.mp3" fadein 2.0

        erz "Im Konferenzzimmer herrscht bedrückte Stille. Die Professoren sitzen um einen grünen Tisch. Nervosität und Verlegenheit liegen in der Luft. Rektor Sonnenstich steht schweigend, die Stirn gerunzelt, während die anderen auf ihre Hände starren."

        sonnenstich "Meine Herren, wir stehen vor einem Abgrund. Die Tragödie des Schülers Stiefel hat unsere Institution erschüttert. Die Öffentlichkeit wird uns beobachten."
        knueppeldick "Ich glaube nicht, dass wir diese Verantwortung allein tragen sollten. Die Anforderungen an die Schüler… sind vielleicht zu hoch."
        fliegentod "Zu hoch? Unsere Aufgabe ist es, sie zu gebildeten Bürgern zu formen. Die Schwäche dieses Jungen war bedauerlich, aber nicht unser Fehler."
        zungenschlag "I-ich möchte daran erinnern, dass wir hier eine Verantwortung gegenüber der Gesellschaft haben."
        hungergurt "Aber was ist mit der Verantwortung gegenüber den Schülern selbst? Waren wir zu streng? Haben wir genug getan, um Stiefel zu unterstützen?"

        stop music fadeout 1.0
        play music "emotional_happy.mp3" fadein 2.0

        sonnenstich "Die Presse wird gnadenlos sein. Wir können nur hoffen, dass unser hoher Standard und unser Ruf uns schützen werden."
        erz "Ein schweres Schweigen legt sich über den Raum. Die Männer blicken sich gegenseitig an, als suche jeder einen Ausweg. Doch keiner spricht es laut aus: Der Tod von Moritz Stiefel ist eine Last, die sie tragen müssen."

        stop music fadeout 2.0
        jump schwangerschaft

    else:

        scene schule
        with fade

        play music "dissonant.mp3" fadein 2.0

        erz "Das Konferenzzimmer liegt in kaltem Licht. Melchior steht vor den Professoren, bleich, aber gefasst. Auf dem Tisch liegt das Schriftstück, das ihn belasten soll."

        sonnenstich "Melchior, dieses gefundene Schriftstück lässt uns keine Wahl. Es ist eindeutig, dass Sie der Autor dieser schamlosen Abhandlung sind."
        mel "Ja, ich habe es geschrieben."
        sonnenstich "Und Sie erkennen die Auswirkungen nicht? Sie haben Stiefel mit Ihrer Verworfenheit in den Abgrund gestoßen!"
        mel "Das ist nicht wahr. Moritz hat sich das Leben genommen, weil er in einem erdrückenden System gefangen war. Nicht mein Schriftstück hat ihn zerstört, sondern Ihre Schule."

        stop music fadeout 1.0
        play music "suspence.mp3" fadein 2.0

        fliegentod "Ungeheuerlich!"
        zungenschlag "E-es ist unerhört!"
        sonnenstich "Sie werden die Konsequenzen tragen. Sie haben Ihre Mitschüler verführt und den Ruf dieser Anstalt beschmutzt."
        mel "Wenn Sie glauben, mein Schweigen hätte Moritz gerettet, irren Sie sich. Glauben Sie ruhig weiter an Ihre Unfehlbarkeit."
        sonnenstich "Führen Sie ihn hinunter!"

        erz "Mit einer stummen Geste weist Sonnenstich den Pedell an, Melchior hinauszuführen. Die Professoren sehen ihm nach, ihre Gesichter starr oder voll heimlicher Erleichterung, die Verantwortung von sich geschoben zu haben."

        stop music fadeout 2.0

        scene black with fade

        play music "very_dark.mp3" fadein 2.0

        erz "Nach dem Auffinden eines problematischen Briefes, in dem Melchior angeblich eine Verfehlung gesteht, stehen seine Eltern vor einer schweren Entscheidung. Sie schicken ihn in eine Jugendkorrektionsanstalt."

        erz "In dieser Anstalt herrschen unmenschliche Bedingungen. Melchior spürt die Ungerechtigkeit, die ihn umgibt. Doch anstatt sich zu fügen, plant er seine Flucht."
        scene wald-sad
        erz "In einer mondlosen Nacht entkommt Melchior aus der Korrektionsanstalt. Entschlossen, seine Freiheit zurückzugewinnen, bricht er auf."

        stop music fadeout 2.0
        jump schwangerschaft

label wendlas_geburtstag_wohnzimmer:

    scene wohnzimmer
    with fade

    play music "emotional_happy.mp3" fadein 2.0

    show mom_happy at left
    show wen_happy at right

    wen "Oh, Mutter! Ein Kleid?"


    mom "Dein Geburtstagskleid. Es wird dir stehen, mein Schatz."

    hide wen_happy
    show wen_unhappy at right
    wen "Aber… warum ist es so lang? Es geht mir ja bis zu den Knöcheln!"

    mom "Du bist jetzt vierzehn, Wendla. Es gehört sich, dass du dich anständig kleidest."

    wen "Aber meine anderen Kleider sind kürzer! Warum darf ich sie nicht weiter tragen?"

    hide mom_happy
    show mom_unhappy at left
    mom "Die Zeiten ändern sich. Du bist kein Kind mehr. Was sollen die Leute denken, wenn du wie ein kleines Mädchen herumlaufst?"

    wen "Aber das hat doch bisher niemanden gestört. Es ist doch nur ein Kleid!"

    mom "Wendla, bitte. Es ist doch besser, sich passend zu kleiden, als… als Aufmerksamkeit auf sich zu ziehen."

    wen "Aufmerksamkeit? Wieso sollte ein Kleid Aufmerksamkeit erregen?"

    mom "Wendla, das verstehst du noch nicht. Und das musst du auch nicht. Zieh es an, und wir reden nicht weiter darüber."

    wen "Ich verstehe nicht, warum es so wichtig ist…"

    mom "Ich weiß, was gut für dich ist. Mehr musst du nicht wissen."

    hide wen_unhappy
    show wen at right
    wen "Mutter, ich will es nicht. Ich bin doch noch ein Kind, oder nicht?"

    mom "Wendla..."

    wen "Warum sollte ich etwas tragen, was ich nicht mag? Es ist mein Geburtstag. Lass mich wenigstens diesen Sommer so bleiben, wie ich bin."

    mom "Vielleicht… Diesen Sommer kannst du noch dein altes Kleid tragen. Nur diesen Sommer."

    hide wen
    show wen_happy at right
    wen "Danke, Mutter."

    stop music fadeout 2.0

    jump moritz_melchior_schule

label schwangerschaft:
    if wendla_aufklaerung == "biologisch":
        jump friedhof_szenen

    scene wohnzimmer with fade

    play music "dissonant.mp3" fadein 2.0

    show mom_unhappy at left
    show wen_unhappy at right

    erz "Das Zimmer ist abgedunkelt. Wendla liegt blass und erschöpft im Bett. Neben ihr sitzt Frau Bergmann, Sorge und Verzweiflung zeichnen ihr Gesicht. Der Medizinalrat Dr. von Brausepulver hat soeben den Raum verlassen."

    erz "Die Diagnose lautet auf 'Bleichsucht', doch Wendla spürt, dass etwas anderes nicht stimmt."

    wen "O Mutter, ich fühle, dass etwas mit mir nicht stimmt. Es ist nicht die Bleichsucht. Es ist etwas anderes."

    hide mom_unhappy
    show mom_happy at left
    mom "Du musst dir keine Sorgen machen, mein Kind. Es wird wieder besser werden."

    erz "Frau Bergmann ringt mit sich selbst. Ihre Fassade bröckelt, Tränen steigen in ihre Augen, während Wendla sie verzweifelt ansieht."

    wen "Mutter, warum weinst du?"

    hide mom_happy
    show mom_unhappy at left
    mom "Wendla, du… du hast ein Kind."

    erz "Wendla starrt ihre Mutter an, die Augen weit aufgerissen."

    wen "Das kann nicht sein. Ich bin doch nicht verheiratet…"

    mom "Das ist das Fürchterliche, mein Kind!"

    wen "Ich weiß es nicht mehr… Wir lagen im Heu…"

    erz "Es klopft an der Tür, doch es ist nur die Nachbarin, die zufällig vorbeikommt. Wendla bleibt zurück, in ihrem Bett, gefangen in einer Welt, die sie nicht versteht."

    stop music fadeout 2.0
    scene black with fade
    mom "Wendla, mein Schlatz, komm mal kurz ins Wohnzimmer. Die Nachbarin will dir helfen..."
    jump friedhof_szenen
