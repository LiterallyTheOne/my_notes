Pytorch notes
=============

Main structure
--------------

Imports
^^^^^^^

.. code-block:: python

    import torch
    from torch import nn

    import torchvision


Define the device that we are going to use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    device = 'cpu'

    if torch.cuda.is_available():
        device = 'cuda'
    elif torch.backends.mps.is_available():
        device ='mps'

    print(f'device: {device}')

Load data
^^^^^^^^^

.. code-block:: python

    train_data = torchvision.datasets.MNIST(
        root='data', train=True, transform=torchvision.transforms.ToTensor(), download=True)

    test_data = torchvision.datasets.MNIST(
        root='data', train=False, transform=torchvision.transforms.ToTensor(), download=True)

.. code-block:: python

    batch_size = 64

    train_data_loader = torch.utils.data.DataLoader(
        train_data, batch_size=batch_size)

    test_data_loader = torch.utils.data.DataLoader(
        test_data, batch_size=batch_size)

Create model
^^^^^^^^^^^^

.. code-block:: python

    class MyModel(nn.Module):

        def __init__(self) -> None:
            super().__init__()
            self.linear_stack = nn.Sequential(
                nn.Flatten(),
                nn.Linear(28*28, 512),
                nn.ReLU(),
                nn.Linear(512, 512),
                nn.ReLU(),
                nn.Linear(512, 10)
            )

        def forward(self, x):
            results = self.linear_stack(x)
            return results


.. code-block:: python

    my_model = MyModel()

    my_model = my_model.to(device)

Define loss function and optimizer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(my_model.parameters(), lr=1e-3)

Define train function
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python


    def train(model: nn.Module, data_loader: torch.utils.data.DataLoader, loss_fn: nn.Module, optimizer: torch.optim.Optimizer, device:str='cuda'):
        number_of_batches = len(data_loader)
        model.train()
        for i, (images, labels) in enumerate(data_loader):
            images = images.to(device)
            labels = labels.to(device)

            prediction = model(images)
            loss = loss_fn(prediction, labels)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            if i % 500 == 0:
                # print(labels)
                # print(prediction.argmax(1))
                print(f'{i+1}/{number_of_batches}, loss = {loss.item():>4f}')

Define test function
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def test(model: nn.Module, data_loader: torch.utils.data.DataLoader, loss_fn: nn.Module, device:str='cuda') -> (torch.float, torch.float):
        data_size = len(data_loader.dataset)
        number_of_batches = len(data_loader)

        model.eval()

        loss = 0
        correct = 0
        with torch.no_grad():
            for images, labels in data_loader:
                images = images.to(device)
                labels = labels.to(device)

                prediction = model(images)
                loss += loss_fn(prediction, labels).item()
                correct += (prediction.argmax(1) ==
                            labels).type(torch.float).sum().item()

            loss /= number_of_batches
            correct /= data_size

        return correct, loss

Train the model and print test results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    for epoch in range(5):
        print(f'in epoch: {epoch}')
        train(my_model, train_data_loader, loss_fn, optimizer, device)
        accuracy, loss = test(my_model, test_data_loader, loss_fn, device)
        print(f'accuracy: {accuracy:.2f}, loss: {loss:.2f}')

Save the model
^^^^^^^^^^^^^^

.. code-block:: python

    torch.save(my_model.state_dict(), "my_model.pth")

Load the model
^^^^^^^^^^^^^^

.. code-block:: python

    loaded_model = MyModel().to(device)
    loaded_model.load_state_dict(torch.load('my_model.pth'))