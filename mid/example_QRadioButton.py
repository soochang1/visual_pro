import torchio as tio
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# TorchIO를 사용하여 데이터셋을 불러오고 전처리를 수행합니다.
def preprocess_images(image_paths, output_shape):
    # 이미지 불러오기
    subjects = []
    for path in image_paths:
        subject = tio.Subject(
            t1=tio.ScalarImage(path),
        )
        subjects.append(subject)
    
    # 전처리 파이프라인 정의
    preprocessing = tio.Compose([
        # 여기에 필요한 전처리 단계를 추가할 수 있습니다.
        tio.Resample(output_shape, image_interpolation='nearest'),
        tio.ZNormalization(),
    ])
    
    # 전처리 파이프라인 적용
    dataset = tio.SubjectsDataset(subjects, transform=preprocessing)
    
    return dataset

# scikit-learn을 사용하여 추가 전처리를 수행합니다.
def additional_preprocessing(data):
    # 이미지 데이터를 벡터 형태로 변환
    images = [subject['t1'][tio.DATA].numpy().flatten() for subject in data]
    
    # 표준 스케일링을 사용하여 데이터 스케일 조정
    scaler = StandardScaler()
    images_scaled = scaler.fit_transform(images)
    
    return images_scaled

# 이미지 파일 경로
image_paths = ['c:/project/lgg-mri-segmentation-metadata']

# 전처리된 이미지 데이터셋 생성
output_shape = (128, 128, 128)  # 출력 이미지 모양
preprocessed_data = preprocess_images(image_paths, output_shape)

# scikit-learn을 사용하여 추가 전처리 수행
processed_data = additional_preprocessing(preprocessed_data)

# 데이터셋을 train, validation, test로 나눔
train_data, test_valid_data = train_test_split(processed_data, test_size=0.3, random_state=42)
valid_data, test_data = train_test_split(test_valid_data, test_size=1/3, random_state=42)


# 처리된 데이터를 사용하여 머신러닝 모델 학습 등을 수행할 수 있습니다.


