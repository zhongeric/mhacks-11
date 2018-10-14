func showAdultInstructionsImage(step: String) {
    var comb = "adult" + step
    switch comb {
    case "adult1":
        displayTextField.text = "Put the person on his or her back on a firm surface"
    case "adult2":
        displayTextField.text = "Kneel next to the person's neck and shoulders"
    case "adult3":
        displayTextField.text = "Place the heel of one hand over the center of the person's chest between the nipples"
    case "adult4":
        displayTextField.text = "Place your other hand on top of the first hand. Keep your elbows straight and position your shoulders directly above your hands"
    case "adult5":
        displayTextField.text = "Use your upper body weight (not just your arms) as you push straight down on (compress) the chest at least 2 inches (approximately 5 centimeters) but not greater than 2.4 inches (approximately 6 centimeters). Push hard at a rate of 100 to 120 compressions a minute"
    case "adult6":
        displayTextField.text = "If you've performed 30 chest compressions open the person's airway using the head-tilt chin-lift maneuver put your palm on the person's forehead and gently tilt the head back"
    case "adult7":
        displayTextField.text = "With the other hand gently lift the chin forward to open the airway"
    case "adult8":
        displayTextField.text = "With the airway open (using the head-tilt chin-lift maneuver) pinch the nostrils shut for mouth-to-mouth breathing"
    case "adult9":
        displayTextField.text = "Cover the person's mouth with yours making a seal"
    case "adult10":
        displayTextField.text = "Prepare to give two rescue breaths. Give the first rescue breath — lasting one second — and watch to see if the chest rises. If it does rise give the second breath. If the chest doesn't rise repeat the head-tilt chin-lift maneuver and then give the second breath. Thirty chest compressions followed by two rescue breaths is considered one cycle. Be careful not to provide too many breaths or to breathe with too much force"
    case "adult11":
        displayTextField.text = "Resume chest compressions to restore circulation"
    case "adult12":
        displayTextField.text = "As soon as an automated external defibrillator (AED) is available  apply it and follow the prompts. Administer one shock  then resume CPR — starting with chest compressions — for two more minutes before administering a second shock. If you're not trained to use an AED  a 911 or other emergency medical operator may be able to guide you in its use. If an AED isn't available continue CPR"
    case "adult13":
        displayTextField.text = "Continue CPR until there are signs of movement or emergency medical personnel take over"
    default:
        print("Filler")
    }
}

func showChildInstructionsImage(step: String) {
    var comb = "child" + step
    switch comb {
    case "child1":
        displayTextField.text = "If you are alone and didn't see the child collapse  perform five cycles of compressions and breaths on the child — this should take about two minutes — before calling 911 or your local emergency number and getting the AED  if one is available"
    case "child2":
        displayTextField.text = "if you are alone and you did see the child collapse  call 911 or your local emergency number and get the AED  if one is available  before beginning CPR. If another person is available  have that person call for help and get the AED while you begin CPR"
    case "child3":
        displayTextField.text = "Put the child on his or her back on a firm surface"
    case "child4":
        displayTextField.text = "Kneel next to the child's neck and shoulders"
    case "child5":
        displayTextField.text = "Use two hands  or only one hand if the child is very small to perform chest compressions"
    case "child6":
        displayTextField.text = "Press straight down on (compress) the chest about 2 inches (approximately 5 centimeters). If the child is an adolescent  push straight down on the chest at least 2 inches (approximately 5 centimeters) but not greater than 2.4 inches (approximately 6 centimeters). Push hard at a rate of 100 to 120 compressions a minute"
    case "child7":
        displayTextField.text = "Do 30 compressions followed by two breaths. This is one cycle"
    case "child8":
        displayTextField.text = "With the airway open (using the head-tilt  chin-lift maneuver)  pinch the nostrils shut for mouth-to-mouth breathing and cover the child's mouth with yours  making a seal"
    case "child9":
        displayTextField.text = "Prepare to give two rescue breaths. Give the first rescue breath — lasting one second — and watch to see if the chest rises. If it does rise  give the second breath. If the chest doesn't rise  repeat the head-tilt  chin-lift maneuver and then give the second breath. Be careful not to provide too many breaths or to breathe with too much force"
    case "child10":
        displayTextField.text = "After the two breaths  immediately begin the next cycle of compressions and breaths. If there are two people performing CPR  conduct 15 compressions followed by two breaths"
    case "child11":
        displayTextField.text = "As soon as an AED is available  apply it and follow the prompts. Use pediatric pads if available  for children up to age 8. If pediatric pads aren't available  use adult pads. Administer one shock  then resume CPR — starting with chest compressions — for two more minutes before administering a second shock"
    case "child12":
        displayTextField.text = "If you're not trained to use an AED  a 911 or other emergency medical operator may be able to guide you in its use"
    case "child13":
        displayTextField.text = "Continue until the child moves or help arrives"
    default:
        print("Filler")
    }
}

func showInfantInstructionsImage(step: string) {
    var comb = "infant" + step
    switch comb {
    case "infant1":
        displayTextField.text = "If you know the baby has an airway obstruction  perform first aid for choking"
    case "infant2":
        displayTextField.text = "If you don't know why the baby isn't breathing  perform CPR"
    case "infant3":
        displayTextField.text = "Examine the situation. Stroke the baby and watch for a response  such as movement  but don't shake the baby"
    case "infant4":
        displayTextField.text = "If there's no response  follow the C-A-B procedures below for a baby under age 1 (except newborns  which includes babies up to 4 weeks old) and time the call for help as follows"
    case "infant5":
        displayTextField.text = "If you're the only rescuer and you didn't see the baby collapse  do CPR for two minutes — about five cycles — before calling 911 or your local emergency number and getting the AED. If you did see the baby collapse  call 911 or your local emergency number and get the AED  if one is available  before beginning CPR"
    case "infant6":
        displayTextField.text = "If another person is available  have that person call for help immediately and get the AED while you attend to the baby"
    case "infant7":
        displayTextField.text = "Place the baby on his or her back on a firm  flat surface  such as a table. The floor or ground also will do"
    case "infant8":
        displayTextField.text = "Imagine a horizontal line drawn between the baby's nipples. Place two fingers of one hand just below this line  in the center of the chest"
    case "infant9":
        displayTextField.text = "Gently compress the chest about 1.5 inches (about 4 centimeters)"
    case "infant10":
        displayTextField.text = "Count aloud as you pump in a fairly rapid rhythm. You should pump at a rate of 100 to 120 compressions a minute"
    case "infant11":
        displayTextField.text = "After 30 compressions  gently tip the head back by lifting the chin with one hand and pushing down on the forehead with the other hand"
    case "infant 12":
        displayTextField.text = "Cover the baby's mouth and nose with your mouth"
    case "infant13":
        displayTextField.text = "Prepare to give two rescue breaths. Use the strength of your cheeks to deliver gentle puffs of air (instead of deep breaths from your lungs) to slowly breathe into the baby's mouth one time  taking one second for the breath. Watch to see if the baby's chest rises. If it does  give a second rescue breath. If the chest does not rise  repeat the head-tilt  chin-lift maneuver and then give the second breath"
    case "infant14":
        displayTextField.text = "If the baby's chest still doesn't rise  continue chest compressions"
    case "infant15":
        displayTextField.text = "Give two breaths after every 30 chest compressions. If two people are conducting CPR  give two breaths after every 15 chest compressions"
    case "infant16":
        displayTextField.text = "Perform CPR for about two minutes before calling for help unless someone else can make the call while you attend to the infant"
    case "infant17":
        displayTextField.text = "Continue CPR until you see signs of life or until medical personnel arrive"
    default:
        print("filler")
    }
}
