<?php

/* columns_definitions/column_type.twig */
class __TwigTemplate_e664dce6c2aa3b937f80920a370934f33f41db85bdbc1005beeb56d0b4055189 extends Twig_Template
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
        echo "<select class=\"column_type\"
    name=\"field_type[";
        // line 2
        echo twig_escape_filter($this->env, ($context["column_number"] ?? null), "html", null, true);
        echo "]\"
    id=\"field_";
        // line 3
        echo twig_escape_filter($this->env, ($context["column_number"] ?? null), "html", null, true);
        echo "_";
        echo twig_escape_filter($this->env, (($context["ci"] ?? null) - ($context["ci_offset"] ?? null)), "html", null, true);
        echo "\"";
        // line 4
        if (($this->getAttribute(($context["column_meta"] ?? null), "column_status", array(), "array", true, true) &&  !$this->getAttribute($this->getAttribute(($context["column_meta"] ?? null), "column_status", array(), "array"), "isEditable", array(), "array"))) {
            // line 5
            echo "disabled=\"disabled\"";
        }
        // line 6
        echo ">
    ";
        // line 7
        echo PhpMyAdmin\Util::getSupportedDatatypes(true, ($context["type_upper"] ?? null));
        echo "
</select>
";
    }

    public function getTemplateName()
    {
        return "columns_definitions/column_type.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  39 => 7,  36 => 6,  33 => 5,  31 => 4,  26 => 3,  22 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "columns_definitions/column_type.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/columns_definitions/column_type.twig");
    }
}
