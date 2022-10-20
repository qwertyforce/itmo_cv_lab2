# itmo_cv_lab2
# Теоретическая база  
### Template Matching 
Сопоставление шаблонов - это процесс перемещения шаблона по всему изображению и вычисления сходства между шаблоном и участком изображения. Участок с наибольшим сходством считается участком где находится искомый объект. В данной работе в качестве меры сходства используется L1 расстояние.


### Использование детекторов и дескрипторов локальных признаков
Детектор находит ключевые точки (keypoint), это точки которые наиболее устойчивы к различным трансформациям. Далее, мы вычисляет дескрипторы окрестностей этих точек. Сравнивая дескрипторы, можно определить, насколько схожи окрестности ключевых точек.
В данной работе используется детектор DoG и дескриптор HardNet8[1]. Для матчинга используется метод smnn (second mutual nearest neighbor). Применяется библиотека Kornia[2]

# Описание разработанной системы
Была написана программа на языке Python, которая реализует поиск с помощью template matching и с помощью сравнения локальных признаков. 

# Результаты работы и тестирования системы
Исходное изображение  
<img src="./0.png" width=50% height=50%>   
Шаблон  
<img src="./0_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./0_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./0_hardnet8.png" width=70% height=70%> 
  
Исходное изображение  
<img src="./1.png" width=50% height=50%>   
Шаблон  
<img src="./1_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./1_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./1_hardnet8.png" width=70% height=70%> 
 
Исходное изображение  
<img src="./2.png" width=50% height=50%>   
Шаблон  
<img src="./2_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./2_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./2_hardnet8.png" width=70% height=70%> 
  
Исходное изображение   
<img src="./3.png" width=50% height=50%>   
Шаблон  
<img src="./3_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./3_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./3_hardnet8.png" width=70% height=70%> 
 
Исходное изображение   
<img src="./4.png" width=50% height=50%>   
Шаблон  
<img src="./4_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./4_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8    
<img src="./4_hardnet8.png" width=70% height=70%> 
  
Исходное изображение  
<img src="./5.png" width=50% height=50%>   
Шаблон  
<img src="./5_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./5_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
Не нашел матчей
 
Исходное изображение  
<img src="./6.png" width=50% height=50%>   
Шаблон  
<img src="./6_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./6_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./6_hardnet8.png" width=70% height=70%> 
 
Исходное изображение  
<img src="./7.png" width=50% height=50%>   
Шаблон  
<img src="./7_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./7_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./7_hardnet8.png" width=70% height=70%> 
 
Исходное изображение  
<img src="./8.png" width=50% height=50%>   
Шаблон  
<img src="./8_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./8_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8  
Только 1 матч, нельзя построить прямоугольник  
<img src="./8_hardnet8.png" width=70% height=70%> 
 
Исходное изображение  
<img src="./9.png" width=50% height=50%>   
Шаблон  
<img src="./9_template.png" width=50% height=50%>   
Результаты Template matching  
<img src="./9_template_matching.png" width=50% height=50%>  
Результаты DoG+HardNet8   
<img src="./9_hardnet8.png" width=70% height=70%> 
 
# Выводы по работе
В результате работы алгоритмов, можно заметить, что локальных признаки гораздо более гибкие и работают гораздо точнее. Их минусом является высокие требования к вычислительным ресурсам и медленная скорость работы. 

# Использованные источники
[1] https://arxiv.org/pdf/2007.09699.pdf
[2] https://kornia.readthedocs.io/en/latest/index.html
