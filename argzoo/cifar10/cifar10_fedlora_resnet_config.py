from easydict import EasyDict

exp_args = dict(
    data=dict(dataset='cifar10', data_path='./data/CIFAR10', sample_method=dict(name='dirichlet', alpha=0.5)),
    learn=dict(
        device='cuda:0',
        local_eps=8,
        global_eps=40,
        batch_size=32,
        optimizer=dict(name='sgd', lr=0.02, momentum=0.9),
        # Only fine-tune parameters whose name contain the keyword "fc".
        finetune_parameters=dict(name='contain', keywords=['lora_A', 'lora_B']),
    ),
    model=dict(
        name='lora_resnet',
        input_channel=3,
        class_number=10,
        r=0.2,
        lora_alpha=1,
    ),
    client=dict(name='fedlora_client', client_num=30, test_frac=0.2),
    server=dict(name='base_server'),
    group=dict(
        name='base_group',
        aggregation_method='avg',
        # Only aggregate parameters whose name does not contain the keyword "fc".
        aggregation_parameters=dict(
            name='except',
            keywords=['lora_A', 'lora_B'],
        ),
    ),
    other=dict(test_freq=3, logging_path='./logging/cifar10_fedlora_resnet_dirichlet_05')
)

exp_args = EasyDict(exp_args)

if __name__ == '__main__':
    from fling.pipeline import personalized_model_serial_pipeline

    personalized_model_serial_pipeline(exp_args, seed=0)