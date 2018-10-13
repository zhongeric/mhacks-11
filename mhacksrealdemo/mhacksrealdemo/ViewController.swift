//
//  ViewController.swift
//  mhacksrealdemo
//
//  Created by Eric Zhong on 10/13/18.
//  Copyright © 2018 ericzhong. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var predictionTextField: UITextField!
    
    var model = fruit_random_forest()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        guard let prediction = try? model.prediction(input: fruit_random_forestInput.init(Color: 1.0, Shape: 0.0, Taste: 0.0) ) else {
            return
        }
        print(prediction.classLabel)
        predictionTextField.text = prediction.classLabel
        print(prediction.classProbability)
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

