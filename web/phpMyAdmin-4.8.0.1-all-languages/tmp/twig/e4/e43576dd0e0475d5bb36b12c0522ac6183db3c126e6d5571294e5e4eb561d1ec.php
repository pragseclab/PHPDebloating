<?php

/* table/search/column_comparison_operators.twig */
class __TwigTemplate_7ea2fecfaf7dc1af5fab5ae031b28ca1858d396b665ceed2a298b445d72e0d2c extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<select id=\"ColumnOperator";
        echo twig_escape_filter($this->env, ($context["search_index"] ?? null), "html", null, true);
        echo "\" name=\"criteriaColumnOperators[";
        echo twig_escape_filter($this->env, ($context["search_index"] ?? null), "html", null, true);
        echo "]\">
    ";
        // line 2
        echo ($context["type_operators"] ?? null);
        echo "
</select>
";
    }

    public function getTemplateName()
    {
        return "table/search/column_comparison_operators.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  26 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "table/search/column_comparison_operators.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/table/search/column_comparison_operators.twig");
    }
}
