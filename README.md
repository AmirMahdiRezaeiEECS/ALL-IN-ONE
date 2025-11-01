# ALL-IN-ONE

deep_learning_project/
├── data/
│   ├── raw/
│   │   ├── full_train.csv          # Full primary training dataset
│   │   ├── full_val.csv            # Full primary validation dataset
│   │   ├── full_test.csv           # Full primary test dataset
│   ├── subsets/
│   │   ├── small_train.csv         # Small subset for quick testing and debugging
│   │   ├── small_val.csv           # Small subset for validation during testing
│   │   ├── pretrain_subset.csv     # Subset for pretraining and network initialization
│   │   ├── arch_search_subset.csv  # Subset for architecture search and hyperparameter tuning
│   ├── processed/
│   │   ├── full_train_processed.npy  # Preprocessed full training data
│   │   ├── small_train_processed.npy # Preprocessed small subsets
│   │   └── ...                     # Other processed files
├── models/
│   ├── pretrained/
│   │   ├── pretrained_model.pth    # Pretrained model weights (e.g., from transfer learning)
│   │   ├── pretrained_config.json  # Configuration for pretrained models
│   ├── checkpoints/
│   │   ├── session_1/
│   │   │   ├── checkpoint_epoch_5.pth  # Intermediate checkpoints from smaller sessions
│   │   │   ├── optimizer_state.pth     # Saved optimizer state for resuming
│   │   ├── session_2/
│   │   │   ├── checkpoint_epoch_10.pth
│   │   │   └── ... 
│   ├── final/
│   │   ├── mnist_model_v1.pth      # Final trained models with versioning
│   │   ├── mnist_model_v1_config.json
│   └── architecture_search/
│       ├── arch_candidate_1.pth    # Models from architecture search experiments
│       └── arch_candidate_2.pth
├── src/
│   ├── repositories/
│   │   ├── dataset_repository.py   # Interfaces for loading full/subset datasets
│   │   └── model_repository.py     # Interfaces for loading/saving models, checkpoints
│   ├── utils/
│   │   ├── preprocessing.py        # Data preprocessing (e.g., normalization, augmentation)
│   │   ├── dataset_utils.py        # Utilities to create subsets from primary dataset
│   │   ├── logging.py              # Logging for experiments
│   │   └── metrics.py              # Evaluation metrics for validation
│   ├── training/
│   │   ├── pretraining.py          # Script/module for pretraining phase
│   │   ├── modular_training.py     # Logic for splitting training into smaller sessions
│   │   ├── regularization.py       # Regularization techniques (e.g., dropout, L1/L2)
│   │   ├── optimization.py         # Optimizers and schedulers (e.g., Adam, SGD)
│   │   └── validation.py           # Validation logic and early stopping
│   ├── experiments/
│   │   ├── architecture_search.py  # Script for neural architecture search
│   │   └── hyperparam_tuning.py    # Hyperparameter optimization (e.g., using Optuna)
│   ├── config/
│   │   ├── pretrain_config.yaml    # Config for pretraining
│   │   ├── training_session.yaml   # Config for modular training sessions
│   │   ├── regularization.yaml     # Config for regularization params
│   │   ├── optimization.yaml       # Config for optimizers and learning rates
│   │   └── validation.yaml         # Config for validation strategies
│   ├── pipeline.py                 # Main pipeline integrating all phases
│   └── main.py                     # Entry point with CLI args for phases (e.g., --phase pretrain)
├── tests/
│   ├── test_pipeline.py
│   ├── test_repositories.py
│   ├── test_pretraining.py         # Tests for pretraining module
│   ├── test_modular_training.py    # Tests for session splitting
│   ├── test_regularization.py      # Tests for regularization
│   ├── test_optimization.py        # Tests for optimizers
│   ├── test_validation.py          # Tests for validation
│   └── mocks/
│       ├── mock_dataset_repository.py
│       └── mock_model_repository.py
├── requirements.txt                # Dependencies (e.g., torch, optuna for tuning)
├── README.md                       # Documentation on setup, running phases, creating subsets
└── .gitignore                      # Ignore large data/models, virtual envs
