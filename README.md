# Миникурс по основам Data Science в химии

- `000_prepare_environment` -- подготовка окружения и загрузка данных

### Практика 1
- `001_first_look_at_data` -- форматы представления химических данных
- `002_load_nabla2DFT_metainformatio` -- работа со SMILES из датасета nabla2DFT

### Практика 2
- `003_strong_ML_baseline` -- три базовые решения: Fingerprints+XGBoost, Bag-of-atoms, Bag-of-bonds
- `004_generate_conformations` -- генерация конформаций

### Практика 3
- `005_geometry_optimization` -- оптимизация геометрии полуэмпирическими методами, HF и DFT теориями
- `006_neural_network_potential` -- нейронные потенциалы. MACE, nabla2DFT



# Возможные проблемы

### Размеры величин

Разные области и подходы используют разные единицы измерения:
- Дистанции могут быть в Ang или Bohr
- Энергия может быть в Hartree, eV, kcal/mol, kJ/mol, eV/atom и других величинах
- Из-за этого силы также могут быть в очень разных величинах, так как силы это энергия делённая на расстояние

Проверяйте входные данные и размеры величин на выходе.

### Окружения

Многие библиотеки для химии могут конфликтовать друг с другом. Если это происходит, то создайте новое окружение:

```bash
conda create -n myenv python=3.10
conda activate myenv
pip install jupyter ipykernel
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
```
