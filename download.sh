set -eou pipefail

get_data() {
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/angry.wav
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/disgust.wav
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/fear.wav
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/happy.wav
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/sad.wav
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/surprise.wav
    wget -nc http://www.cs.columbia.edu/~sarahita/CL/MSP_samples/neutral.wav
}

main() {
    get_data
}

main