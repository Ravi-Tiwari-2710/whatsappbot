# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

s = '\xe0\xa4\xb9\xe0\xa5\x80 \xe0\xa4\xac\xe0\xa5\x8b\xe0\xa4\xb2' 
s.encode('raw-unicode-escape').decode('utf-8')


app = Flask(__name__)

@app.route("/wasms", methods=['POST'])

# chatbot logic
def bot():
    msg = request.form.get('Body').lower() # Reading the message from the whatsapp
 
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()
    # Create reply
 
    # Text response
    if  "hi" in msg:
       reply.body("hi,we provide the following services: 1-solution for crop diseases. 2-fertilizer and pesticides recommendation. 3-Seed recommandation for crops. 4-Information about Government Schemes. 5-Contect Helpline. 6-Weather Information. 7-Know your Farm Report.")
    elif "fertilizer for cotton" in msg:
        reply.body("Amruth Organic Cotton Grow https://agribegri.com/products/buy-micronutrients-for-plants--micronutrients-ferrtilizers--.php and Trichoderma Viride Anti Fungal Bio Fertilizerhttps://seed2plant.in/products/trichoderma-viride?currency=INR&utm_medium=cpc&utm_source=google&utm_campaign=SmartShoppingSeeds&gclid=CjwKCAjwu5yYBhAjEiwAKXk_eEhW8LdLMc9VRIbtssaSOF3bo383Si_fOzkyUFIZt49NNvF_GWjsARoCQJoQAvD_BwE")
    elif "seed for cotton" in msg:
        reply.body("Goldi 21 Re. Hybrid Castor Seed https://agribegri.com/products/buy-castor-seeds--castor-seeds-online--castor-hybrid-seeds-.php")
    elif "fertilizer for sugercane" in msg:
        reply.body("Nuttrivate Arka Citrus Special https://agribegri.com/products/crop-specific-micronutrient-technology.php Utkarsh SOP https://agribegri.com/products/hui-1.php")
    elif "seed for orange" in msg:
        reply.body("MARIGOLD GULZAFRI ORANGE SEEDS https://www.allthatgrows.in/products/marigold-gulzafri-orange-seeds?utm_source=google&utm_medium=cpc&utm_campaign=Google-Shopping-Listings&gclid=CjwKCAjwu5yYBhAjEiwAKXk_eNY4U81wK5BVeqybpokywX6D8h_jkril5RmsRUpFfOUOowMXwmPUXhoCkf4QAvD_BwE")
    elif "fertilizer for orange" in msg:
        reply.body("Nuttrivate Arka Citrus Special https://agribegri.com/products/crop-specific-micronutrient-technology.php")
    elif "fertilizer for potato" in msg:
        reply.body("Anshul Potato Special https://www.agriplexindia.com/potato-special.html?srsltid=AdGWZVQHu8SaA32d7ZBbPaxVTBShODSfA_jLb4wO9cjtIEmSUEiHVwxU_kI")
    elif "helpline number" in msg:
        reply.body("HELPLINE NO. OF YOUR LOCAL EXPERT :+918979880333")
    elif "weather" in msg:
        reply.body("Possibility of rain is in next 5 days in your area.")
    elif "report" in msg:
        reply.body("report https://drive.google.com/file/d/1ZG-LbhtsWafRHSooTqulpj2aIRAnGnnG/view?usp=sharing")
    elif "नमस्ते" in msg:
        reply.body("नमस्ते, हम निम्नलिखित सेवाएं प्रदान करते हैं: 1-फसल रोगों के लिए समाधान। 2-उर्वरक और कीटनाशकों की सिफारिश। 3-फसलों के लिए बीज की सिफारिश। 4-सरकारी योजनाओं की जानकारी। 5-संपर्क हेल्पलाइन। 6-मौसम की जानकारी। 7-अपनी फार्म रिपोर्ट जानें।")
    elif "कपास की खाद" in msg:
        reply.body("Amruth Organic Cotton Grow https://agribegri.com/products/buy-micronutrients-for-plants--micronutrients-ferrtilizers--.php and Trichoderma Viride Anti Fungal Bio Fertilizerhttps://seed2plant.in/products/trichoderma-viride?currency=INR&utm_medium=cpc&utm_source=google&utm_campaign=SmartShoppingSeeds&gclid=CjwKCAjwu5yYBhAjEiwAKXk_eEhW8LdLMc9VRIbtssaSOF3bo383Si_fOzkyUFIZt49NNvF_GWjsARoCQJoQAvD_BwE")
    elif "कपास का बीज" in msg:
        reply.body("Goldi 21 Re. Hybrid Castor Seed https://agribegri.com/products/buy-castor-seeds--castor-seeds-online--castor-hybrid-seeds-.php")
    elif "संतरे का उर्वरक" in msg:
        reply.body("Nuttrivate Arka Citrus Special https://agribegri.com/products/crop-specific-micronutrient-technology.php")
    elif "गन्ने की खाद" in msg:
        reply.body("Nuttrivate Arka Citrus Special https://agribegri.com/products/crop-specific-micronutrient-technology.php Utkarsh SOP https://agribegri.com/products/hui-1.php")
    elif "संतरे का बीज" in msg:
        reply.body("MARIGOLD GULZAFRI ORANGE SEEDS https://www.allthatgrows.in/products/marigold-gulzafri-orange-seeds?utm_source=google&utm_medium=cpc&utm_campaign=Google-Shopping-Listings&gclid=CjwKCAjwu5yYBhAjEiwAKXk_eNY4U81wK5BVeqybpokywX6D8h_jkril5RmsRUpFfOUOowMXwmPUXhoCkf4QAvD_BwE")
    elif "मौसम" in msg:
        reply.body("आपके क्षेत्र में अगले 5 दिनों में बारिश की संभावना है।")
    elif "रिपोर्ट" in msg:
        reply.body("report:https://drive.google.com/file/d/1ZG-LbhtsWafRHSooTqulpj2aIRAnGnnG/view?usp=sharing")

    return str(resp)
 
    

    


if __name__ == "__main__":
	app.run()



