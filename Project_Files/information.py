class Information:
    summary = "Quick Charge can be defined as a technology introduced by Qualcomm, implemented on Snapdragon chipsets, " \
              "which focuses on pushing in more power, so as to charge the device battery faster. \n\nQuick Charge is a " \
              "proprietary technology that allows for the charging of battery-powered devices, primarily mobile phones, " \
              "at power levels exceeding the 5 volts at 2 amps, thus 10 watts allowed by basic USB standards —not " \
              "considering the USB Power Delivery (USB PD) standard—while still maintaining compatibility to existing USB " \
              "wires. "

    charge_1 = "Well, it all started with Qualcomm Quick Charge 1.0 and as you can expect, the devices that are " \
               "compatible with Quick Charge 1.0 would now be considered old. Quick Charge 1.0 is able to draw 2.0A " \
               "current of power from nearly any source that it’s connected to and this allows for faster charging with " \
               "more power being supplied to a device. Version 1.0 was only capable of using 5 volt supply of power, " \
               "though. Quick Charge 1.0 today is basically what can be seen as “Normal Charging” today, back then " \
               "pushing the 2.0A envelope was fast enough but times have changed. "

    charge_2 = "Then came Qualcomm Quick Charge 2.0 and this is where things got interesting. Many devices featured the " \
               "Snapdragon processor that was compatible with Quick Charge 2.0, and this time the charging truly exceeded " \
               "the expectations of the users. Voltage-wise Quick Charge 2.0 tech has options of \n5v/ 9v/ 12v which meant " \
               "more power and the max current of 3A which was a one up from the traditional Quick Charge. Also, " \
               "Quick Charge " \
               "2.0 introduced an optional feature called Dual Charge (initially called Parallel Charging), using two " \
               "PMICs to split the power into 2 streams to reduce phone temperature. "

    charge_3 = "Quick Charge 3.0 is engineered to refuel devices up to four times faster than conventional charging. It " \
               "is designed to charge twice as fast as Quick Charge 1.0 and to be 38 percent more efficient than Quick " \
               "Charge 2.0. Now consumers can spend even less time charging, and can grab and go more quickly.Quick " \
               "Charge 3.0 employs Intelligent Negotiation for Optimum Voltage INOV (Intelligent Negotiation for Optimal " \
               "Voltage), an algorithm which allows your " \
               "portable device to determine what power level to request at any point in time, enabling optimum power " \
               "transfer while maximizing efficiency. It also supports wider voltage options, allowing a mobile device to " \
               "dynamically adjust to the ideal voltage level supported by that specific device. Specifically, " \
               "Quick Charge 3.0 offers a more granular range of voltages: 200mV increments, from 3.6V to 20V. \nThat way " \
               "your phone can target one of dozens of power levels."

    charge_4 = "QC 4.0 also includes the latest iteration of Qualcomm's custom power management algorithm, Intelligent " \
               "Negotiation for Optimum Voltage (INOV). Additions include real-time thermal management, which will " \
               "regulate the temperature during power delivery to keep things safer and more efficient. New power " \
               "management ICs are also part of the picture and will come with QC 4-ready devices. \nQuick Charge 4 " \
               "includes HVDCP++, optional Dual Charge++, INOV 3.0, and Battery Saver Technologies 2. It is " \
               "cross-compatible with both USB-C and USB PD specifications, supporting fallback to USB PD if either the " \
               "charger or device is not compatible. \nHowever, Quick Charge 4 chargers are not backward compatible with " \
               "Quick Charge. "

    charge_4_1 = "Quick Charge 4+ was announced on June 1, 2017. It introduces Intelligent Thermal Balancing and Advanced " \
                 "Safety Features to eliminate hot spots and protect against overheating and short-circuit or damage to " \
                 "the " \
                 "USB-C connector. Dual Charge++ is mandatory, while in prior versions Dual Charge was optional. \nUnlike " \
                 "Quick Charge 4, Quick Charge 4+ is fully backward compatible with Quick Charge C 2.0 and 3.0 devices. "

    charge_5 = "Quick Charge 5 was announced on July 27, 2020. With up to 100 W of power, on a mobile phone with a 4500 " \
               "mAh battery, Qualcomm claims 50% charge in just 5 minutes. Qualcomm announced that this standard is " \
               "cross-compatible with USB PD PPS programmable power supply, and that its technology can communicate with " \
               "the charger when charging double cells and double the voltage and amperage out. \n\nFor instance, " \
               "a single battery requests 8.8 V of power. The dual cell can then ask the PPS charger to output 17.6 volts " \
               "and split it in half to the two separate battery, pulling 5.6 amps total to achieve 100 watts. The first " \
               "phone with this technology was the Xiaomi Mi 10 Ultra. "

    usb_1 = "USB-C (formally known as USB Type-C) is a 24-pin USB connector system with a rotationally symmetrical " \
            "connector. The designation C refers only to the connector's physical configuration or form factor and " \
            "should not be confused with the connector's specific capabilities, which are designated by its transfer " \
            "specifications (such as USB 3.2). \n\nUSB-C cables interconnect hosts and devices, replacing various other " \
            "electrical cables and connectors, including USB-A and USB-B, HDMI, DisplayPort, and 3.5mm audio jacks. " \
            "\n\nUSB " \
            "Type-C and USB-C are trademarks of USB Implementers Forum."

    usb_2 = "The USB Type-C Specification 1.0 was published by the USB Implementers Forum (USB-IF) and was finalized in " \
            "August 2014. It was developed at roughly the same time as the USB 3.1 specification. In July 2016, " \
            "it was adopted by the IEC as 'IEC 62680-1-3'. USB-C brings with it a lot of benefits. Extra pins allow " \
            "for increased data, " \
            "video and power deliveries. USB-C can now support up to 40GBps. " \
            "This does " \
            "improve 5 times upon a standard USB 3.0 port’s 5 Gbit/s and 20 times faster than USB 2.0’s 480 Mbit/s " \
            "speeds.\n\nUSB-C plugged into a USB 3.1 port: Capable of transfer speeds up 10 gigabytes of data per second. " \
            "\nUSB-C plugged into a USB 3.2 port: Capable of transfer speeds up to 20 gigabytes per second.\nA " \
            "Thunderbolt 3 and 4 cables are capable of transferring up to 40 gigabytes of data per second, which is twice " \
            "the " \
            "maximum data transfer speed of USB-C. However, in order to hit these data transfer speeds, you must use a " \
            "Thunderbolt cable with a Thunderbolt port, and not a USB-C port. "

    power_delivery = "Power Delivery (PD) is a specification for handling higher power and allows a range of devices to " \
                     "charge quickly over a USB connection. It operates by facilitating a conversation between two " \
                     "devices to negotiate a power contract so they can determine how much power can be pulled from the " \
                     "charger. Power Delivery starts at the 5V setting and is configurable up to 20V. Using a standard " \
                     "USB-C cable, it can handle up to 60W, and will go up to 100W using a designated EMCA cable. " \
                     "\n\nAnother " \
                     "point of interest regarding Power Delivery is that it allows for power to flow both ways, " \
                     "with no set direction based on circuit or connection. For example, if you were to connect two " \
                     "phones that support Power Delivery with a USB-C charging cable, one phone could charge the other " \
                     "and vice versa. "

    video_output = "Currently, DisplayPort is the most widely implemented alternate mode, and is used to provide video " \
                   "output on devices that do not have standard-size DisplayPort or HDMI ports, such as smartphones and " \
                   "laptops. \nA USB-C multiport adapter converts the device's " \
                   "native video stream to DisplayPort/HDMI/VGA, allowing it to be displayed on an external display, " \
                   "such as a television set or computer monitor. It is also used on USB-C docks designed to connect a " \
                   "device to a power source, external display, USB hub, and optional extra (such as a network port) with " \
                   "a single cable. \n\nThese functions are sometimes implemented directly into the display instead of a " \
                   "separate dock, meaning a user connects their device to the display via USB-C with no other " \
                   "connections required. "

    downsides = "In conjunction with a Quick Charge technology, USB-C opens up endless possibilities in terms of speed " \
                "and power delivery for modern smartphones. However, with fast-charging batteries, you get less battery " \
                "capacity. \nThere’s a positive pole and a negative one in every battery, however, there’s also a " \
                "separator " \
                "that keeps the electrons from jumping directly to the other side. The electrons are directed through a " \
                "circuit so that you get the electricity created from them. The problem arises with the fast charging " \
                "batteries since to keep the battery stable at a high speed of charging, you need to make the separator " \
                "in the middle thicker, which means less battery capacity. The actual amount of usable battery or battery " \
                "density becomes lower. \nNew smartphones with super-fast or ultra charging sometimes even need to split " \
                "the battery area into two individual batteries because of the separator, which would need to be even " \
                "bigger. \nAll this leads to less battery capacity, and there is no workaround for it so far. "