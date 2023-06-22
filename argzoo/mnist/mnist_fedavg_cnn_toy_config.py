from easydict import EasyDict

exp_args = dict(
    data=dict(dataset='mnist', data_path='./data/mnist', sample_method=dict(name='iid')),
    learn=dict(
        device='cuda:0',
        local_eps=1,
        global_eps=4,
        batch_size=32,
        loss='CrossEntropyLoss',
        optimizer=dict(name='sgd', lr=0.02, momentum=0.9)
    ),
    model=dict(
        name='cnn',
        input_channel=1,
        class_number=10,
    ),
    client=dict(name='base_client', client_num=30),
    server=dict(name='base_server'),
    group=dict(name='base_group', aggregation_method='avg'),
    other=dict(test_freq=3, logging_path='./logging/mnist_fedavg_cnn_iid_demo')
)

exp_args = EasyDict(exp_args)

if __name__ == '__main__':
    from fling.pipeline import general_model_serial_pipeline
    general_model_serial_pipeline(exp_args, seed=0)