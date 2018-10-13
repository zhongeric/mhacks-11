//
//  ViewController.swift
//  mhacks
//
//  Created by Eric Zhong on 10/12/18.
//  Copyright © 2018 ericzhong. All rights reserved.
//

import UIKit
import CoreML
import AVFoundation
import AVKit
import Speech
import Alamofire
import SwiftyJSON

class ViewController: UIViewController, AVAudioRecorderDelegate, SFSpeechRecognizerDelegate {
    
    @IBAction func apiCallButton(_ sender: Any) {
        Alamofire.request("http://35.1.220.104:5000/?query=he%20laying%20table").responseJSON { response in
            print("Request: \(String(describing: response.request))")   // original url request
            print("Response: \(String(describing: response.response))") // http url response
            print("Result: \(response.result)")                         // response serialization result
            
            if let json = response.result.value {
                print("JSON: \(json)") // serialized json response
                let json_loads = JSON(response.result.value)
            }
            
            if let data = response.data, let utf8Text = String(data: data, encoding: .utf8) {
                print("Data: \(utf8Text)") // original server data as UTF8 string
            }
            return json_loads
        }
    }
    @IBOutlet weak var displayTextField: UITextField!
    @IBOutlet weak var recordButton: UIButton!
    @IBAction func recordButton(_ sender: Any) {
        recordTapped()
    }
    func createDirectory() -> URL {
        let audioFilename = getDocumentsDirectory().appendingPathComponent("recording.m4a")
        return audioFilename
    }
    @IBAction func readAudioButton(_ sender: Any) {
        requestTranscribePermissions()
        let audioFilename = createDirectory()
        transcribeAudio(url: audioFilename)
    }
    
    //var recordButton: UIButton!
    var recordingSession: AVAudioSession!
    var audioRecorder: AVAudioRecorder!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        recordingSession = AVAudioSession.sharedInstance()
        requestTranscribePermissions()
        
        do {
            try recordingSession.setCategory(AVAudioSessionCategoryPlayAndRecord)
            try recordingSession.setActive(true)
            recordingSession.requestRecordPermission() { [unowned self] allowed in
                DispatchQueue.main.async {
                    if allowed {
                        print("allowed!")
                        //self.loadRecordingUI()
                    } else {
                        // failed to record!
                        print("Not allowed")
                    }
                }
            }
        } catch {
            print("Failed to record, caught")
            // failed to record!
        }
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    @objc func recordTapped() {
        if audioRecorder == nil {
            startRecording()
        } else {
            finishRecording(success: true)
        }
    }
    
    func getDocumentsDirectory() -> URL {
        let paths = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)
        return paths[0]
    }
    
    func requestTranscribePermissions() {
        SFSpeechRecognizer.requestAuthorization { [unowned self] authStatus in
            DispatchQueue.main.async {
                if authStatus == .authorized {
                    print("Good to go!")
                } else {
                    print("Transcription permission was declined.")
                }
            }
        }
    }
    
    func finishRecording(success: Bool) {
        audioRecorder.stop()
        audioRecorder = nil
        let audioFilename = createDirectory()
        
        if success {
            recordButton.setTitle("Tap to Re-record", for: .normal)
            transcribeAudio(url: audioFilename)
        } else {
            recordButton.setTitle("Tap to Record", for: .normal)
            // recording failed :(
        }
    }
    
    func startRecording() {
        
        let audioFilename = getDocumentsDirectory().appendingPathComponent("recording.m4a")
        
        let settings = [
            AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
            AVSampleRateKey: 12000,
            AVNumberOfChannelsKey: 1,
            AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
        ]
        
        do {
            audioRecorder = try AVAudioRecorder(url: audioFilename, settings: settings)
            audioRecorder.delegate = self
            audioRecorder.record()
            
            recordButton.setTitle("Tap to Stop", for: .normal)
        } catch {
            finishRecording(success: false)
        }
    }
    
    func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool) {
        if !flag {
            finishRecording(success: false)
        }
    }
    
    func transcribeAudio(url: URL) {
        // create a new recognizer and point it at our audio
        let recognizer = SFSpeechRecognizer()
        let request = SFSpeechURLRecognitionRequest(url: url)
        
        // start recognition!
        recognizer?.recognitionTask(with: request) { [unowned self] (result, error) in
            // abort if we didn't get any transcription back
            guard let result = result else {
                print("There was an error, no transcription received: \(error!)")
                return
            }
            
            // if we got the final transcription back, print it
            if result.isFinal {
                // pull out the best transcription...
                print(result.bestTranscription.formattedString)
            }
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

