# Stream24

Real-time object detection and video streaming using OpenCV, MobileNet-SSD, and MediaMTX.

## Overview

Stream24 is a lightweight computer vision pipeline that performs real-time object detection on video streams using the MobileNet-SSD deep learning model and OpenCV. The processed frames can be streamed through MediaMTX, enabling low-latency video analytics for surveillance, monitoring, edge AI, and streaming applications.

The project demonstrates how to combine:

- Real-time video capture
- Deep learning–based object detection
- RTSP/stream processing
- MediaMTX streaming infrastructure
- Lightweight deployment on commodity hardware

---

## Features

- Real-time object detection using MobileNet-SSD
- OpenCV-based video processing pipeline
- Stream ingestion and forwarding
- MediaMTX integration
- Low-latency inference
- Simple and portable architecture
- Easy local deployment

---

## Project Structure

text stream24/ │ ├── MobileNetSSD_deploy.caffemodel ├── MobileNetSSD_deploy.prototxt │ ├── main.py ├── detect_stream.py ├── stream_test.py │ ├── mediamtx.yml ├── requirements.txt │ └── README.md 

### Key Components

| File | Description |
|--------|------------|
| main.py | Main application entry point |
| detect_stream.py | Object detection and inference pipeline |
| stream_test.py | Stream validation/testing utility |
| mediamtx.yml | MediaMTX configuration |
| MobileNetSSD_deploy.prototxt | Model architecture definition |
| MobileNetSSD_deploy.caffemodel | Pretrained MobileNet-SSD weights |

---

## Detection Classes

MobileNet-SSD can detect common object categories including:

- Person
- Car
- Bus
- Bicycle
- Motorbike
- Dog
- Cat
- Chair
- Bottle
- TV Monitor

and several other COCO/VOC object classes.

---

## Installation

### Clone Repository

bash git clone https://github.com/nnfuad/stream24.git cd stream24 

### Create Virtual Environment

bash python -m venv venv source venv/bin/activate 

### Install Dependencies

bash pip install -r requirements.txt 

---

## Running MediaMTX

Start the MediaMTX server:

bash mediamtx 

Or use the provided configuration:

bash mediamtx mediamtx.yml 

---

## Run Object Detection

bash python main.py 

or

bash python detect_stream.py 

---

## Stream Testing

Validate incoming streams using:

bash python stream_test.py 

---

## Architecture

text Video Source       │       ▼  OpenCV Capture       │       ▼  MobileNet-SSD       │       ▼  Bounding Boxes       │       ▼  MediaMTX       │       ▼  RTSP / Network Stream 

---

## Example Applications

- Smart surveillance
- Traffic monitoring
- Campus security
- Edge AI deployments
- Industrial monitoring
- Live stream analytics
- Object-aware video pipelines

---

## Performance Notes

Performance depends on:

- CPU/GPU hardware
- Input resolution
- Frame rate
- Number of objects in scene

For edge deployments, reducing input resolution can significantly improve throughput and latency.

---

## Future Improvements

- YOLOv8 integration
- GPU acceleration
- Multi-camera support
- Object tracking
- Web dashboard
- Docker deployment
- Stream recording
- Event-based alerts

---

## Tech Stack

- Python
- OpenCV
- MobileNet-SSD
- Caffe
- MediaMTX

---

## Author

Nur Nafis Fuad

Electrical and Computer Engineering  
Machine Learning & Computer Vision Enthusiast

---

## License

This project is released under the MIT License.