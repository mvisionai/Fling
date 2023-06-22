from easydict import EasyDict

exp_args = dict(
    data=dict(dataset='cifar100', data_path='./data/CIFAR100', sample_method=dict(name='dirichlet', alpha=0.2)),
    learn=dict(
        device='cuda:0',
        local_eps=8,
        global_eps=40,
        batch_size=32,
        loss='CrossEntropyLoss',
        optimizer=dict(name='sgd', lr=0.02, momentum=0.9),
        finetune_parameters=dict(name='contain', keywords=['fc']),
    ),
    model=dict(
        name='cifar_resnet',
        input_channel=3,
        class_number=100,
    ),
    client=dict(name='base_client', client_num=30, test_frac=0.2),
    server=dict(name='base_server'),
    group=dict(
        name='base_group',
        aggregation_method='avg',
        aggregation_parameters=dict(
            name='except',
            keywords=['fc'],
        ),
    ),
    other=dict(test_freq=3, logging_path='./logging/cifar100_fedper_resnet_dirichlet_02')
)

exp_args = EasyDict(exp_args)

if __name__ == '__main__':
    from fling.pipeline import personalized_model_serial_pipeline

    personalized_model_serial_pipeline(exp_args, seed=0)