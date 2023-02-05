# Planning-related thoughts
# Important content:


### How do we want to do this?
After research into openCV there seems to be several ways to face this problem. \
Most likely we will want to use haar-cascades which are a very easy way to identify objects in images. 

There are already haar-cascades available for person identification. Is the goal to train our own? \
This seems like the most interesting approach to me.

Training a haar-cascade for trash recognition should be simple enough. We need a negative set and a positive set and hours on a decent performing computer. \
Tensorflow has a good negative set.


### What do we want to do?
I think it might be good after initial research to rephrase our goal: \
Create an application that can identify littering and alert the owner of the software. \
It will do this by Identifying litter, identifying whether a person is present by the litter and alerting by email \
( Specialized software integration may be useful at a later stage.)

### Who are our customers?
We may have as customers any land or facility proprietor. \
Public areas governed by municipalities (beaches, city centers) \
Authorities in an attempt to reduce littering in cities. 

Another thing to consider is that the software can be used with some negatives too. \
A restauranteaur may use this software to identify cleaning needs, to observe tables with litter that there are no people by. (May be very applicable to fast-food restaurants) 

### Useful quotes

In the same vein, MJU [33](https://paperswithcode.com/dataset/mju-waste) is another dataset for segmentation; however, unlike TACO, this dataset contains only indoor images with people holding the litter instances in their hands. 

The TACO dataset [37] presents 1500 images involving 4784 annotations, where most of the annotations are considered as large, with images ranging from 842×474
 to 6000×4000
 pixels. 

#### Links
##### Datasets
 - [Drinking waste classification](https://paperswithcode.com/dataset/drinking-waste-classification) 
 - [UAVVASTE](https://paperswithcode.com/dataset/uavvaste)
 - [Garbage dataset kaggle](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification?resource=download)

##### Models
 - [Efficientdet_d0](https://docs.openvino.ai/2021.2/omz_models_public_efficientdet_d0_tf_efficientdet_d0_tf.html) 
 - [Yolo_v5](https://towardsdatascience.com/how-to-train-a-custom-object-detection-model-with-yolo-v5-917e9ce13208)

##### Information / Research Papers
[R-CNN](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)
[Overfeat paper](https://arxiv.org/abs/1312.6229)

[YOLOv1](https://arxiv.org/pdf/1506.02640.pdf)
[YOLOv5](https://www.mdpi.com/2076-3417/12/14/7255/pdf)
### Questions for Furth
På vilket sätt rekommenderas presentationen läggas upp? Vi kommer naturligtvis hålla ett demo och har diskuterat småskaligt hur vi skall göra detta. \
Men mer specifikt fördelningen Demo/Sales pitch mot kodpresentation? \
Då vår egentliga publik är medstuderande samt programansvariga kanske det är intressant att ha en viss fokus på "How" \
Lista över potentiell publik: 
- Köpare
- Tech-ansvariga
- Användare
- Jurister
- Medstudenter (Att bryta fjärde väggen?)
- Teknikintresserade

Upplägget på presentationen kommer att bero till stor del på vilka antaganden vi gör. \
I en naturlig demo kanske intressenterna är Köpare Tech-ansvariga användare och jurister.

##### Sustainability perspective
"During your project presentation, you will dedicate one part/slide of the presentation to explaining your project from a sustainability-perspective."
Är denna verkligen nödvändig med det projekt vi har? Det är ju lite intuitivt i produktbeskrivningen. \
Tankar på vad man hade kunnat inkludera här.

##### Flera Modeller
Skulle du kunna repetera dina tankar om att lära in flera modeller? 

##### Mini-inlärning
Hur testar man olika metoder på ett projekt med så mycket data som detta? \
Vi kommer behöva experimentera lite med olika bildmanipulationer om vi inte bara följer någon "Best-practice"-guide. 

Hur avgör man tillförlitlighet i en modell om man minskar sample-size i testning?





# Presentations-Outline

### Introduction
Kanske starta med ett extremt kortfattat intro av vad vi kommer presentera?

#### Presentation av gruppen
 - Namn
 - Bakgrund
 - Interaktiv Roadmap?

### Demo
 - Vad kommer produkten förändra
 - Vad finns det för problem i branchen/området i nuläget?
 - Demo
   - Ha en film redo med visualiseringar
   - Kanske Livedemo  (Hade varit snyggt att kunna ta en bild på klassen där man illustrerar vilka människor som stökar ner)
   - Visa vårt Front-end UI (Är detta verkligen en faktisk komponent av vår MVP eller har vi front-end enbart för demo?)
### Tekniska förklaringar
 - Ge en enkel översikt för hur produkten fungerar tekniskt på en hög nivå.
 - Hur tränar man en Haar-Cascade?
 - Exempelkod - Kanske presentera med en snygg städad notebook. Markdown cheat-sheet över funktionerna som används?

### Reflektioner
 - Individuella reflektioner över projektets gång
 - Vad är framtiden för produkten
 - Vad är potentiella förbättringar för produkten



### Tankar till gruppen

1. En idé för visualisering. Om vi kör på tanken med litter detection & person detection som två separata modeller, så kan man visualisera litter färgkodat med närmsta person mha. euklidiskt avstånd mot medelpunkterna. \
Detta kan vara väldigt snyggt i stora grupper människor

2. Efter lite undersökning av situationen kommer jag till misstanken att vi kanske borde hitta en nisch och istället om tid finns bredda till fler modeller. \
Detta kan innebära att vi väljer en plats, typ "Kontor" som grund för vårt negativa dataset. \ 
Problemet med en generell "Trash detection" är att vi kommer ha väldigt svårt att bestämma negativ data för klassifikation som inte förvirrar modellen. Det vill säga data som inte innehåller föremålen vi klassifierar. \ 
Dessa antaganden gjorde jag i samband med reflektionerna i [Litter_detection_with_deep_learning](https://www.mdpi.com/1424-8220/22/2/548#sec4dot3-sensors-22-00548)

3. Det finns ett problem med små föremål typ cigarettfimpar och liknande i att det kan ta väldigt lång tid att träna en modell på hög upplösning, samt att hitta en bra nivå av "blur". 

4. Är det kanske mer lämpligt att använda en enkel edge-cascade för trash-detection? \
Konvertera till HSV? \
Fördelar och nackdelar med metoderna? Kanske lite utanför scope vad jag förväntar mig att ni undersökt just nu, men viktiga tankar och då det kan ta väldigt lång tid att lära in modellerna kan det vara bra att testa lite.

5. Det finns många förtränade haar-cascades för ansiktsigenkänning och personidentifiering som kan användas vid tidsbrist.
6. Det kan tydligen vara svårt att få hög accuracy med hemmagjorda haar-cascades.
7. Vi kan behöva bestämma ett datum då våra modeller är "inte röra" så att vi kan göra färdigt övriga delar av projektet.

#### Application performance
På något vis borde vi tänka på hur vi skall presentera förutsägningarna. Hur gör vi en välpresterande modell som samtidigt kan ha en bred informationsnivå? \
Jag gillar email-tanken då den inte kräver direkt respons så tycker definitivt att detta är startpunkten.

### Front-end
**Plugin till smartphone** 

Hade varit extremt snyggt för att demonstrera produkten. Kanske mindre användbart praktiskt?

**Flask / Dash** \
Enkelt. Går att göra snygga front-ends och visualisera bilder på ett tydligt sätt. \
Kanske att ha detta som bas för administration av produkten? \
Hade varit coolt att kunna presentera en video-stream där man slänger lite skräp live.
